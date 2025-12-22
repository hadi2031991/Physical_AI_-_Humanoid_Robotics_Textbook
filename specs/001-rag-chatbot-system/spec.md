# Feature Specification: RAG Chatbot System

**Feature Branch**: `001-rag-chatbot-system`
**Created**: 2025-12-10
**Status**: Draft
**Input**: User description: "Build a complete, production-ready RAG system..."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Ingestion (Priority: P1)

As a site administrator, I want to ingest the book's content into the system so that it can be queried by the chatbot.

**Why this priority**: This is the foundational step required for the chatbot to have any knowledge to draw from. Without it, no Q&A is possible.

**Independent Test**: After running the ingestion process for a sample document, I can verify that the corresponding data (chunks, embeddings) exists in the vector and metadata stores.

**Acceptance Scenarios**:
1. **Given** a collection of markdown files representing the book, **When** the administrator triggers the `/ingest` endpoint, **Then** the system successfully processes the files, creates text chunks and embeddings, and stores them in Qdrant and Neon Postgres.
2. **Given** new or updated content, **When** the ingestion process is run again, **Then** the system updates the knowledge base accordingly without creating duplicates.

---

### User Story 2 - Global Question Answering (Priority: P2)

As a reader, I want to open the chatbot on any page, ask a question, and receive an answer generated from the context of the entire book.

**Why this priority**: This is the primary value proposition for the end-user, providing a powerful search and summarization tool for the book.

**Independent Test**: I can open the chatbot, ask a question like "What is the main idea of Chapter 3?", and receive a relevant, coherent answer.

**Acceptance Scenarios**:
1. **Given** the chatbot widget is open, **When** I type a question and press enter, **Then** the chatbot displays a streamed response that is relevant to my question and based on the book's content.
2. **Given** I ask a question outside the scope of the book, **When** the chatbot generates a response, **Then** it should indicate that it does not have information on that topic.

---

### User Story 3 - Contextual Question Answering (Priority: P3)

As a reader, I want to highlight a specific piece of text on the page, and ask the chatbot a clarifying question about that selection.

**Why this priority**: This provides a more focused and powerful user experience for understanding specific sections of the text.

**Independent Test**: I can select a paragraph of text, open the chatbot, and ask "Can you explain this in simpler terms?". The answer should be based *only* on the selected text.

**Acceptance Scenarios**:
1. **Given** I have selected a piece of text on the page, **When** I open the chatbot and ask a question, **Then** the frontend sends my question, the selected text, and the page context to the backend.
2. **Given** the backend receives a query with selected text, **When** it generates an answer, **Then** the RAG process should strongly prioritize the selected text as the primary context.

### Edge Cases
- What happens if the user selects a very large block of text? (e.g., >10,000 characters)
- How does the system handle ingestion of non-markdown files or malformed content?
- What is the expected response when no relevant context is found for a global question?
- How is the chat history managed for returning users?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: System MUST provide a backend service built with FastAPI.
- **FR-002**: System MUST provide an `/ingest` endpoint for processing and storing book content.
- **FR-003**: The ingestion process MUST chunk text, generate embeddings, and store data in Qdrant Cloud and Neon Serverless Postgres.
- **FR-004**: System MUST provide an `/ask` endpoint to handle user questions, performing a RAG process to generate answers.
- **FR-005**: System MUST provide a `/health` endpoint for status checks.
- **FR-006**: The generation process MUST use OpenAI models. The specific generation model (e.g., gpt-4-turbo, gpt-3.5-turbo) should be configurable via environment variables or a configuration file, allowing flexibility to balance cost and quality.
- **FR-007**: The ingestion process MUST use an automatic text chunking strategy. The chunking strategy should be Semantic Chunking to optimize retrieval quality by grouping semantically related text. Parameters (chunk size, overlap) will be determined during the research phase.
Authentication for the /ingest endpoint will be via Admin Credentials, requiring a username and password. This provides a secure method suitable for administrative access.
- **FR-009**: The frontend MUST be a React component embedded as a widget in the Docusaurus site.
- **FR-010**: The frontend MUST capture user-selected text from the browser's `window.getSelection()` API.
- **FR-011**: The chat widget MUST stream responses back to the user interface.

### Key Entities *(include if feature involves data)*
- **Document**: A representation of a single source document (e.g., a chapter markdown file) containing its content and metadata.
- **Chunk**: A segment of text derived from a Document, forming the basis for vector search. Each chunk is associated with its source Document.
- **ChatMessage**: A record of a single turn in a conversation, including the user's query, the system's response, and associated context.
- **Conversation**: A collection of ChatMessages that form a single, continuous interaction with a user.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: 95% of `/ask` requests should receive the first token of a streamed response in under 3 seconds.
- **SC-002**: The ingestion process for 100 markdown pages (avg. 2000 words each) must complete in under 5 minutes.
- **SC-003**: The chatbot frontend widget must have a negligible impact on the Docusaurus site's PageSpeed score (i.e., not decrease it by more than 5 points).
- **SC-004**: User satisfaction with answer relevance, measured via a 1-5 star rating in the chat widget, must average >= 4.0.