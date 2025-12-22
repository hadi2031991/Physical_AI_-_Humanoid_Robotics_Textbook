---
title: RAG Chatbot
emoji: 🤖
colorFrom: blue
colorTo: red
sdk: docker
pinned: false
license: mit
---

# RAG Chatbot

This Space demonstrates a Retrieval-Augmented Generation (RAG) chatbot that allows you to upload documents and ask questions about them using a Hugging Face language model.

## Features

- Upload PDF, DOCX, or TXT documents
- Ask questions about your documents
- Get context-aware responses from a Hugging Face language model
- Simple and intuitive interface

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

## Configuration

By default, the application uses the `microsoft/DialoGPT-small` model. You can change this by setting the `HF_MODEL_NAME` environment variable to any compatible causal language model from Hugging Face Hub.

## Limitations

- Documents are stored in memory and will be lost when the space restarts
- Large documents may be truncated for performance reasons
- The default model is small for fast inference but may not be as accurate as larger models

## License

This project is licensed under the MIT License.