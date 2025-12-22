# Tasks: RAG Chatbot System

**Input**: Design documents from `/specs/001-rag-chatbot-system/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This task list includes tests to ensure the robustness and correctness of the implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend API**: `rag-chatbot-api/src/`, `rag-chatbot-api/tests/`
- **Frontend App**: `book-docusaurus-site/src/`
- Paths shown below are adjusted for the project's backend/frontend structure.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `rag-chatbot-api` project directory `rag-chatbot-api/`
- [X] T002 Initialize Python project in `rag-chatbot-api/` with `venv`
- [X] T003 Create `rag-chatbot-api/requirements.txt` with initial dependencies (FastAPI, uvicorn, openai, qdrant-client, psycopg2-binary, python-dotenv)
- [X] T004 Create `rag-chatbot-api/.env.example` for environment variables
- [X] T005 [P] Configure linting (e.g., Black, Flake8) for `rag-chatbot-api/`
- [X] T006 [P] Configure formatting (e.g., isort) for `rag-chatbot-api/`
- [X] T007 Update `.gitignore` in `rag-chatbot-api/` for Python project
- [X] T008 Configure `book-docusaurus-site/.env.example` for frontend API endpoint

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Implement base database configuration and connection in `rag-chatbot-api/src/db.py`
- [X] T010 Implement Pydantic models for Document, Chunk, Conversation, ChatMessage in `rag-chatbot-api/src/models/`
- [ ] T011 [P] Implement Alembic (or similar) for database migrations in `rag-chatbot-api/`
- [ ] T012 [P] Implement basic authentication for admin credentials in `rag-chatbot-api/src/auth.py`
- [ ] T013 [P] Implement Qdrant client initialization and connection in `rag-chatbot-api/src/vector_db.py`
- [ ] T014 [P] Implement OpenAI client initialization and model configuration in `rag-chatbot-api/src/llm.py`
- [ ] T015 Create `rag-chatbot-api/src/main.py` with FastAPI app instance and include `/health` router
- [ ] T016 Implement `/health` endpoint in `rag-chatbot-api/src/api/health.py` checking DB and Vector DB status
- [ ] T017 [P] Implement basic logging configuration in `rag-chatbot-api/src/utils/logger.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Content Ingestion (P1) 🎯 MVP

**Goal**: Admin ingests book content.

**Independent Test**: After running the ingestion process for a sample document, verify that the corresponding data (chunks, embeddings) exists in the vector and metadata stores.

### Implementation for User Story 1

- [ ] T018 [US1] Create Qdrant collection setup logic in `rag-chatbot-api/src/vector_db.py`
- [ ] T019 [US1] Implement database migrations for Document and Chunk tables
- [ ] T020 [US1] Implement `Document` service (CRUD operations) in `rag-chatbot-api/src/services/document_service.py`
- [ ] T021 [US1] Implement `Chunk` service (CRUD operations) in `rag-chatbot-api/src/services/chunk_service.py`
- [ ] T022 [US1] Implement text loading and preprocessing (e.g., markdown parsing) in `rag-chatbot-api/src/core/ingestion.py`
- [ ] T023 [US1] Implement Semantic Chunking logic in `rag-chatbot-api/src/core/ingestion.py`
- [ ] T024 [US1] Implement embedding generation using OpenAI in `rag-chatbot-api/src/core/ingestion.py`
- [ ] T025 [US1] Implement storage of chunks and embeddings in Qdrant in `rag-chatbot-api/src/core/ingestion.py`
- [ ] T026 [US1] Implement storage of document metadata in Neon Postgres in `rag-chatbot-api/src/core/ingestion.py`
- [ ] T027 [US1] Implement `/ingest` API endpoint with admin authentication in `rag-chatbot-api/src/api/ingestion.py`
- [ ] T028 [US1] Add integration tests for `/ingest` endpoint in `rag-chatbot-api/tests/integration/test_ingestion.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Global Question Answering (P2)

**Goal**: Reader asks global questions.

**Independent Test**: Open the chatbot, ask a question like "What is the main idea of Chapter 3?", and receive a relevant, coherent answer.

### Implementation for User Story 2

- [ ] T029 [US2] Implement retrieval from Qdrant based on user query in `rag-chatbot-api/src/core/retrieval.py`
- [ ] T030 [US2] Implement RAG orchestration for global Q&A (query + retrieved chunks) in `rag-chatbot-api/src/core/rag.py`
- [ ] T031 [US2] Implement response generation using configurable OpenAI model (streaming) in `rag-chatbot-api/src/llm.py`
- [ ] T032 [US2] Implement `Conversation` and `ChatMessage` services in `rag-chatbot-api/src/services/chat_service.py`
- [ ] T033 [US2] Implement `/ask` API endpoint for global Q&A (streaming response) in `rag-chatbot-api/src/api/chat.py`
- [ ] T034 [US2] Implement basic chat UI component in `book-docusaurus-site/src/components/Chatbot/index.tsx`
- [ ] T035 [US2] Implement API client in `book-docusaurus-site/src/services/api.ts` to call backend `/ask` endpoint
- [ ] T036 [US2] Add component tests for global Q&A UI in `book-docusaurus-site/src/components/Chatbot/index.test.tsx`
- [ ] T037 [US2] Add integration tests for `/ask` endpoint (global Q&A) in `rag-chatbot-api/tests/integration/test_chat.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Contextual Question Answering (P3)

**Goal**: Reader asks questions on selected text.

**Independent Test**: Select a paragraph of text, open the chatbot, and ask "Can you explain this in simpler terms?". The answer should be based *only* on the selected text.

### Implementation for User Story 3

- [ ] T038 [US3] Enhance `book-docusaurus-site/src/components/Chatbot/index.tsx` to detect user text selection (`window.getSelection()`)
- [ ] T039 [US3] Modify `book-docusaurus-site/src/services/api.ts` to send selected text and page context to `/ask` endpoint
- [ ] T040 [US3] Enhance RAG orchestration in `rag-chatbot-api/src/core/rag.py` to prioritize selected text for context
- [ ] T041 [US3] Add integration tests for contextual Q&A via `/ask` endpoint in `rag-chatbot-api/tests/integration/test_chat.py`
- [ ] T042 [US3] Add component tests for contextual Q&A UI in `book-docusaurus-site/src/components/Chatbot/index.test.tsx`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T043 [P] Configure Dockerfile for `rag-chatbot-api`
- [ ] T044 [P] Implement deployment instructions for Qdrant, Neon, FastAPI (Render/Fly.io), and Docusaurus (GitHub Pages)
- [ ] T045 [P] Create example RAG queries and use cases in `docs/examples/`
- [ ] T046 [P] Code cleanup and refactoring in both `rag-chatbot-api/` and `book-docusaurus-site/`
- [ ] T047 [P] Review and optimize database queries for performance
- [ ] T048 [P] Add unit tests for core RAG logic in `rag-chatbot-api/tests/unit/`
- [ ] T049 [P] Update `README.md` for both backend and frontend projects with setup and usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
