# RAG Chatbot for Hugging Face Spaces

This is a Retrieval-Augmented Generation (RAG) chatbot that allows you to upload documents and ask questions about them using a Hugging Face language model. The application is built with Gradio for easy deployment on Hugging Face Spaces.

## Features

- Upload PDF, DOCX, or TXT documents
- Ask questions about your documents
- Get context-aware responses from a Hugging Face language model
- Simple and intuitive interface

## Deploy to Hugging Face Spaces

1. **Create a new Space**:
   - Go to [https://huggingface.co/new-space](https://huggingface.co/new-space)
   - Give your space a name (e.g., "my-rag-chatbot")
   - Select "Docker" as the SDK
   - Choose "CPU" (or "GPU" if you want faster inference)
   - Make it public or private as per your preference
   - Click "Create Space"

2. **Add the files to your Space**:
   You can either:
   
   **Option A: Using Git (recommended)**
   ```bash
   git clone https://huggingface.co/spaces/<your-username>/<your-space-name>
   cd <your-space-name>
   
   # Copy all files from this repository to your space directory
   # Then push the changes
   git add .
   git commit -m "Add RAG chatbot application"
   git push
   ```
   
   **Option B: Upload directly**
   - Go to your Space page
   - Click on "Files" tab
   - Upload all files from this repository:
     - `app.py` (main application)
     - `requirements.txt` (dependencies)
     - `Dockerfile` (container configuration)
     - `.env` (configuration file)
     - `README.md` (for the space description)

3. **Configure your environment** (optional):
   - Create a `.env` file with the following content:
   ```
   HF_MODEL_NAME=microsoft/DialoGPT-small
   ```
   - You can change the model to any compatible causal language model from Hugging Face Hub

4. **Wait for the Space to build**:
   - After uploading the files, the Space will automatically start building
   - Check the "Logs" tab to see the build progress
   - The first build may take several minutes as it downloads the model

## How to Use

1. Upload a document using the "Upload Document" button
2. Select the document you want to query from the dropdown
3. Type your question in the chat box and press Enter or click "Send"
4. The chatbot will provide a response based on the content of your document

## Technical Details

This application uses:
- **Gradio** for the web interface
- **Hugging Face Transformers** for the language model (default: microsoft/DialoGPT-small)
- **Sentence Transformers** for embedding generation
- **PyPDF2** and **docx2txt** for document processing

The RAG (Retrieval-Augmented Generation) pipeline:
1. Extracts text from uploaded documents
2. Uses the document content as context for the language model
3. Generates context-aware responses to user queries

## Recommended Models

You can change the `HF_MODEL_NAME` environment variable to use different models:

- `microsoft/DialoGPT-small` - Lightweight and fast (default)
- `microsoft/DialoGPT-medium` - Better quality, larger
- `gpt2` - General purpose model
- `distilgpt2` - Faster, smaller GPT-2 variant
- `facebook/opt-350m` - Good performance-to-size ratio

## Limitations

- Documents are stored in memory and will be lost when the space restarts
- Large documents may be truncated for performance reasons
- The default model is small for fast inference but may not be as accurate as larger models

## Troubleshooting

- **Model loading errors**: The first run may take longer due to model downloading. Subsequent runs will be faster.
- **Memory issues**: If you encounter memory issues, try using a smaller model.
- **Slow responses**: For faster responses, consider using a GPU instance on Hugging Face Spaces.

## License

This project is licensed under the MIT License.