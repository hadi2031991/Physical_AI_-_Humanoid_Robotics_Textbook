import os
import uuid
import tempfile
from typing import List, Optional
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from starlette.responses import JSONResponse

from .db import get_db, init_db, init_engine
from .models.models import Document as DocumentModel, Chunk as ChunkModel, \
    Conversation as ConversationModel, ChatMessage as ChatMessageModel, DocumentCreate, DocumentResponse, \
    ChatMessageCreate, ChatMessageResponse, ConversationResponse

# Import Hugging Face components
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import torch
from PyPDF2 import PdfReader
import docx2txt

load_dotenv()

app = FastAPI(
    title="RAG Chatbot API",
    description="An API for a Retrieval-Augmented Generation (RAG) chatbot using Hugging Face models.",
    version="0.1.0"
)

# Initialize Hugging Face models
# Using a lightweight model for demonstration - can be changed to any model
model_name = os.getenv("HF_MODEL_NAME", "microsoft/DialoGPT-small")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize sentence transformer for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Global document store for simple RAG implementation
document_store = {}

@app.on_event("startup")
async def on_startup():
    """Initialize the database."""
    # Initialize database engine and tables
    init_engine()
    await init_db()

@app.get("/health", summary="Health Check", description="Check if the API is running.")
async def health_check():
    """
    Health check endpoint to ensure the API is running.
    """
    return JSONResponse(content={"status": "ok"})


def extract_text_from_file(file_path: str, file_ext: str) -> str:
    """Extract text from file based on its extension."""
    if file_ext.lower() == '.pdf':
        pdf_reader = PdfReader(file_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file_ext.lower() in ['.docx', '.doc']:
        return docx2txt.process(file_path)
    elif file_ext.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_ext}")


# API Endpoints
@app.post("/documents", summary="Upload a document", description="Upload a new document for processing.",
          response_model=DocumentResponse)
async def upload_document(
        file: UploadFile = File(...),
        title: str = Form(...),
        source_path: str = Form(...),
        db: AsyncSession = Depends(get_db)
):
    """
    Uploads a document, extracts text, and stores metadata in the database.
    """
    # Create a temporary file to save the uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as tmp_file:
        content = await file.read()
        tmp_file.write(content)
        tmp_file_path = tmp_file.name

    try:
        # Calculate checksum
        checksum = str(uuid.uuid5(uuid.NAMESPACE_DNS, content.decode('utf-8', errors='ignore')))

        # Extract text from the document
        file_ext = Path(file.filename).suffix
        document_text = extract_text_from_file(tmp_file_path, file_ext)

        # Create document record in DB
        doc = DocumentModel(title=title, source_path=source_path, checksum=checksum)
        db.add(doc)
        await db.commit()
        await db.refresh(doc)

        # Store document text in our simple in-memory store
        # In a real application, you'd want to store this in a persistent store or embed it
        document_store[str(doc.id)] = document_text

        # For now, we'll also create chunk records in the database (though they won't hold the actual embeddings)
        # Split the text into chunks for reference
        chunk_size = 1000
        overlap = 200
        start = 0
        chunk_order = 0
        chunk_models = []

        while start < len(document_text):
            end = start + chunk_size
            chunk_text = document_text[start:end]

            chunk_id = uuid.uuid4()
            chunk = ChunkModel(
                id=chunk_id,
                document_id=doc.id,
                text=chunk_text[:200] + "..." if len(chunk_text) > 200 else chunk_text,  # Store first 200 chars
                chunk_order=chunk_order
            )
            chunk_models.append(chunk)

            start = start + chunk_size - overlap
            chunk_order += 1

        db.add_all(chunk_models)
        await db.commit()

        return doc

    except Exception as e:
        # Clean up the temporary file in case of error
        if os.path.exists(tmp_file_path):
            os.unlink(tmp_file_path)
        raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

    finally:
        # Clean up the temporary file
        if os.path.exists(tmp_file_path):
            os.unlink(tmp_file_path)


@app.post("/chat", summary="Chat with the RAG model", description="Send a query to the chatbot and get a response.",
          response_model=ChatMessageResponse)
async def chat_with_rag_model(
        chat_message: ChatMessageCreate,
        db: AsyncSession = Depends(get_db)
):
    """
    Takes a user query, retrieves relevant document context, and generates a response using Hugging Face model.
    """
    if not document_store:
        raise HTTPException(status_code=400, detail="No documents have been uploaded yet. Please upload a document first.")

    # Get document text from our simple store
    # In a real implementation, you would use embeddings and vector search
    # For this simplified version, we'll use the first document
    doc_id = next(iter(document_store))
    document_text = document_store[doc_id]

    # Create a context by taking a portion of the document text
    # In a real implementation, you would perform semantic search to find relevant chunks
    context = document_text[:3000]  # Take first 3000 chars as context

    # Create a prompt with the context and user query
    prompt = f"""
    You are a helpful assistant. Answer the user's query based on the provided context.

    Context: {context}

    Query: {chat_message.query}

    Please provide a helpful and accurate response based on the context provided. If the context doesn't contain the information needed to answer the query, please indicate that.
    """

    try:
        # Tokenize the input
        inputs = tokenizer.encode(prompt, return_tensors="pt")

        # Generate response using the model
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=inputs.shape[1] + 100,  # Generate up to 100 additional tokens
                num_return_sequences=1,
                temperature=0.7,
                pad_token_id=tokenizer.eos_token_id,
                do_sample=True,
                top_k=50,
                top_p=0.95
            )

        # Decode the generated response
        llm_response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Remove the original prompt from the response to get just the answer
        if prompt in llm_response:
            llm_response = llm_response[len(prompt):].strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response with Hugging Face model: {str(e)}")

    # Get or create conversation
    if chat_message.conversation_id:
        conversation = await db.get(ConversationModel, chat_message.conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = ConversationModel()
        db.add(conversation)
        await db.commit()
        await db.refresh(conversation)

    # Save chat message
    db_chat_message = ChatMessageModel(
        conversation_id=conversation.id,
        query=chat_message.query,
        response=llm_response,
        relevant_chunks=[doc_id],  # For now, just reference the document
        model_used=os.getenv("HF_MODEL_NAME", "microsoft/DialoGPT-small")
    )
    db.add(db_chat_message)
    await db.commit()
    await db.refresh(db_chat_message)

    return db_chat_message


@app.get("/conversations", summary="List all conversations",
          description="Retrieve a list of all conversations.",
          response_model=List[ConversationResponse])
async def list_conversations(db: AsyncSession = Depends(get_db)):
    """
    Retrieves all conversations from the database.
    """
    result = await db.execute(select(ConversationModel))
    conversations = result.scalars().all()
    return conversations


@app.get("/conversations/{conversation_id}", summary="Get a conversation",
          description="Retrieve a specific conversation by its ID.",
          response_model=List[ChatMessageResponse])
async def get_conversation(conversation_id: str, db: AsyncSession = Depends(get_db)):
    """
    Retrieves all messages for a specific conversation.
    """
    conversation = await db.get(ConversationModel, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    result = await db.execute(
        select(ChatMessageModel)
        .where(ChatMessageModel.conversation_id == conversation_id)
        .order_by(ChatMessageModel.timestamp)
    )
    messages = result.scalars().all()
    return messages


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
