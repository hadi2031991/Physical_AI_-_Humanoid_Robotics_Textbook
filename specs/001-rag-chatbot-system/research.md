# Research for RAG Chatbot System

## Clarification Decisions

### Decision 1: OpenAI Generation Model

- **Chosen Option**: Configurable (via environment variables or config file)
- **Rationale**: Provides the best balance of flexibility, allowing the project to adapt to changing cost/quality requirements without code changes. This aligns with a "production-ready" system.
- **Implications**: The backend service (FastAPI) will need to implement a mechanism to load and use the configured model, rather than hardcoding it.

### Decision 2: Text Chunking Strategy

- **Chosen Option**: Semantic Chunking
- **Rationale**: Semantic chunking is expected to yield higher quality RAG results by preserving the contextual meaning within chunks, which is crucial for answering complex questions related to a book's content. This choice prioritizes answer quality over implementation simplicity.
- **Implications**: Implementing semantic chunking will likely be more complex than recursive character splitting or token-based splitting, potentially requiring additional libraries or custom logic in the ingestion pipeline. Parameters like chunk size and overlap will need to be determined and optimized during the research/development phase.

### Decision 3: Ingestion Endpoint Authentication

- **Chosen Option**: Admin Credentials (Username/Password)
- **Rationale**: Provides a more robust and auditable authentication mechanism suitable for administrative actions, especially if multiple administrators need to manage ingestion.
- **Implications**: The FastAPI backend will need to implement a secure user/password authentication system for the `/ingest` endpoint, including credential storage (hashed) and validation. This is more involved than a simple API key but offers better security for administrative access.
