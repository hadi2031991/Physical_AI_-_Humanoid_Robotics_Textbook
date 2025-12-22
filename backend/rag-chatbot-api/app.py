import os
import uuid
import tempfile
from pathlib import Path
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import torch
from PyPDF2 import PdfReader
import docx2txt
import sqlite3
from datetime import datetime

# Initialize Hugging Face models
model_name = os.getenv("HF_MODEL_NAME", "microsoft/DialoGPT-small")
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except:
    # Fallback to a simpler model if the specified one fails
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

# Initialize sentence transformer for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Global document store for simple RAG implementation
document_store = {}

def extract_text_from_file(file_path, file_ext):
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
        raise ValueError(f"Unsupported file type: {file_ext}")


def upload_document(file, title):
    """Upload and process a document."""
    if file is None:
        return "No file provided", ""
    
    # Create a temporary file to save the uploaded file
    file_path = file.name
    file_ext = Path(file_path).suffix
    
    try:
        # Extract text from the document
        document_text = extract_text_from_file(file_path, file_ext)
        
        # Generate a unique document ID
        doc_id = str(uuid.uuid4())
        
        # Store document text in our simple in-memory store
        document_store[doc_id] = {
            'title': title or f"Document {len(document_store)+1}",
            'content': document_text,
            'uploaded_at': datetime.now()
        }
        
        return f"Successfully uploaded: {title or 'Untitled'}", f"Document content preview: {document_text[:500]}..."
    
    except Exception as e:
        return f"Error processing document: {str(e)}", ""


def chat_with_rag(user_input, history, selected_doc_id):
    """Process user input and generate a response using the RAG system."""
    if not document_store:
        return "Please upload a document first to ask questions about it.", history
    
    if not selected_doc_id:
        # Use the first available document if none is selected
        selected_doc_id = next(iter(document_store))
    
    # Get document text from our store
    document_text = document_store[selected_doc_id]['content']
    
    # Create a context by taking a portion of the document text
    context = document_text[:3000]  # Take first 3000 chars as context

    # Create a prompt with the context and user query
    prompt = f"""
    You are a helpful assistant. Answer the user's query based on the provided context.
    
    Context: {context}
    
    Query: {user_input}
    
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
        
        # Update chat history
        history = history + [(user_input, llm_response)]
        return "", history
    
    except Exception as e:
        return f"Error generating response: {str(e)}", history


def get_documents_list():
    """Return a list of uploaded documents for selection."""
    if not document_store:
        return []
    
    return [(doc_id, doc_info['title']) for doc_id, doc_info in document_store.items()]


def create_gradio_interface():
    """Create the Gradio interface."""
    with gr.Blocks(title="RAG Chatbot") as demo:
        gr.Markdown("# 🤖 RAG Chatbot")
        gr.Markdown("Upload documents and ask questions about them!")
        
        # Document upload section
        with gr.Row():
            with gr.Column(scale=1):
                doc_input = gr.File(label="Upload Document", file_types=[".pdf", ".docx", ".txt"])
                doc_title = gr.Textbox(label="Document Title")
                upload_btn = gr.Button("Upload Document")
                upload_status = gr.Textbox(label="Upload Status", interactive=False)
            
            with gr.Column(scale=2):
                doc_preview = gr.Textbox(label="Document Preview", interactive=False)
        
        # Document selection
        doc_selector = gr.Dropdown(label="Select Document to Query", choices=[])
        
        # Chat section
        chatbot = gr.Chatbot(label="Chat with your Documents")
        user_input = gr.Textbox(label="Your Question", placeholder="Ask a question about your document...")
        
        # Buttons
        with gr.Row():
            submit_btn = gr.Button("Send")
            clear_btn = gr.Button("Clear Chat")
        
        # Event handling
        upload_btn.click(
            fn=upload_document,
            inputs=[doc_input, doc_title],
            outputs=[upload_status, doc_preview]
        ).then(
            fn=get_documents_list,
            inputs=[],
            outputs=[doc_selector]
        )
        
        submit_btn.click(
            fn=chat_with_rag,
            inputs=[user_input, chatbot, doc_selector],
            outputs=[user_input, chatbot]
        )
        
        user_input.submit(
            fn=chat_with_rag,
            inputs=[user_input, chatbot, doc_selector],
            outputs=[user_input, chatbot]
        )
        
        clear_btn.click(
            fn=lambda: [[], None],
            inputs=[],
            outputs=[chatbot, doc_selector]
        ).then(
            fn=get_documents_list,
            inputs=[],
            outputs=[doc_selector]
        )
    
    return demo


if __name__ == "__main__":
    iface = create_gradio_interface()
    iface.launch(server_name="0.0.0.0", server_port=7860)