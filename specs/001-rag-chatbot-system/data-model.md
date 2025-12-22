# Data Model for RAG Chatbot System

This document outlines the key entities and their relationships for the RAG Chatbot System.

## Entities

### Document

Represents a single source document (e.g., a chapter markdown file) that has been ingested into the system.

-   **id (UUID)**: Unique identifier for the document.
-   **title (String)**: Title of the document.
-   **source_path (String)**: Original file path or URL of the document.
-   **created_at (Timestamp)**: Timestamp when the document was first ingested.
-   **updated_at (Timestamp)**: Timestamp of the last update to the document content.
-   **checksum (String)**: Hash of the document content to detect changes.
-   **metadata (JSONB)**: Additional metadata (e.g., author, chapter number, section).

### Chunk

Represents a segment of text derived from a `Document`. These chunks are the units stored in the vector database and used for retrieval.

-   **id (UUID)**: Unique identifier for the chunk.
-   **document_id (UUID)**: Foreign key referencing the `Document` it belongs to.
-   **text (Text)**: The actual text content of the chunk.
-   **embedding (Vector)**: The vector representation of the `text`, stored in Qdrant.
-   **chunk_order (Integer)**: The order of this chunk within its parent document.
-   **metadata (JSONB)**: Additional metadata specific to the chunk (e.g., page number, section heading).

### Conversation

Represents a single continuous interaction session with a user.

-   **id (UUID)**: Unique identifier for the conversation.
-   **user_id (UUID/String - Optional)**: Identifier for the user (if authenticated or session-based).
-   **started_at (Timestamp)**: Timestamp when the conversation began.
-   **last_activity_at (Timestamp)**: Timestamp of the last message in the conversation.

### ChatMessage

Represents a single turn (user query and system response) within a `Conversation`.

-   **id (UUID)**: Unique identifier for the chat message.
-   **conversation_id (UUID)**: Foreign key referencing the `Conversation` it belongs to.
-   **query (Text)**: The user's question or prompt.
-   **response (Text)**: The system's generated answer.
-   **timestamp (Timestamp)**: Timestamp when this message was recorded.
-   **relevant_chunks (Array of UUIDs - Optional)**: IDs of `Chunk`s used to generate the response.
-   **selected_text (Text - Optional)**: User-selected text if it was a contextual query.
-   **page_context (Text - Optional)**: Full page content if available from a contextual query.
-   **model_used (String)**: Identifier for the OpenAI model used for generation.
-   **feedback (Integer - Optional)**: User feedback (e.g., 1-5 star rating).

## Relationships

-   A `Document` can have many `Chunk`s (One-to-Many: Document -> Chunk).
-   A `Conversation` can have many `ChatMessage`s (One-to-Many: Conversation -> ChatMessage).
-   `ChatMessage`s are linked to `Document`s via `Chunk`s used for retrieval.
