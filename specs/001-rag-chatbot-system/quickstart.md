# Quickstart Guide: RAG Chatbot System

This guide provides a rapid setup and execution overview for the RAG Chatbot System.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

-   **Python 3.11+**: For the FastAPI backend.
-   **Node.js (LTS)**: For the Docusaurus frontend.
-   **npm / Yarn**: Package managers for Node.js.
-   **Git**: For cloning the repository.
-   **Docker / Docker Compose (Optional)**: For local development environment setup.
-   **OpenAI API Key**: Required for embeddings and response generation.
-   **Neon Serverless Postgres Account**: For the database.
-   **Qdrant Cloud Account**: For the vector database.

## 2. Setup Backend (FastAPI)

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd rag-chatbot-api # Navigate to the backend directory
    ```
2.  **Create a virtual environment and install dependencies**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate # On Windows
    # source venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` will be generated during implementation.)*

3.  **Configure Environment Variables**:
    Create a `.env` file in the `rag-chatbot-api/` directory with the following (replace with your actual keys/credentials):
    ```ini
    OPENAI_API_KEY="your_openai_api_key"
    QDRANT_HOST="your_qdrant_cloud_host"
    QDRANT_API_KEY="your_qdrant_api_key"
    NEON_DATABASE_URL="your_neon_postgres_connection_string"
    ADMIN_USERNAME="your_admin_username"
    ADMIN_PASSWORD="your_admin_password"
    ```

4.  **Run Database Migrations (Neon Postgres)**:
    *(Migration commands will be provided during implementation, e.g., using Alembic.)*
    ```bash
    # Example: alembic upgrade head
    ```

5.  **Start the FastAPI Backend**:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    The API will be accessible at `http://localhost:8000/api/v1`.

## 3. Setup Frontend (Docusaurus)

1.  **Navigate to the frontend directory**:
    ```bash
    cd book-docusaurus-site # From the repository root
    ```
2.  **Install dependencies**:
    ```bash
    npm install # or yarn install
    ```
3.  **Configure API Endpoint**:
    *(This will be done during implementation, typically in `docusaurus.config.ts` or a React context, to point to your FastAPI backend, e.g., `http://localhost:8000/api/v1` for local development.)*

4.  **Start the Docusaurus Development Server**:
    ```bash
    npm start # or yarn start
    ```
    The Docusaurus site will open in your browser, typically at `http://localhost:3000`.

## 4. Ingest Content

Once both backend and frontend are running, you can ingest content.

1.  **Access `/ingest` endpoint**: Use a tool like `curl` or Postman to send a POST request to `http://localhost:8000/api/v1/ingest`.
2.  **Authenticate**: Provide the `ADMIN_USERNAME` and `ADMIN_PASSWORD` via HTTP Basic Auth.
3.  **Request Body**: Send a JSON payload with `content_paths` (e.g., local markdown file paths).
    ```bash
    curl -X POST "http://localhost:8000/api/v1/ingest" \
         -H "Content-Type: application/json" \
         -u "your_admin_username:your_admin_password" \
         -d '{ "content_paths": ["./data/my_chapter.md"] }'
    ```
    *(Note: `./data/my_chapter.md` assumes a `data` directory will be created in the backend service, which will be specified during implementation.)*

## 5. Interact with the Chatbot

1.  **Open Docusaurus site**: `http://localhost:3000`.
2.  **Navigate to a book page**: Ensure content has been ingested.
3.  **Open the Chatbot Widget**: (The UI element to open the chatbot will be implemented on the Docusaurus site).
4.  **Ask Questions**:
    *   Type a question for global Q&A.
    *   Select text on the page and then ask a question for contextual Q&A.

This quickstart provides a basic outline. Further details and specific commands will be provided during the implementation phases.
