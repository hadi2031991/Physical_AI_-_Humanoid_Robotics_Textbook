# Implementation Plan: RAG Chatbot System

**Branch**: `001-rag-chatbot-system` | **Date**: 2025-12-10 | **Spec**: ./spec.md
**Input**: Feature specification from `./spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a complete, production-ready RAG system that includes a FastAPI backend for content ingestion and Q&A, and a React-based chatbot widget embedded in a Docusaurus frontend. The system must support global and contextual Q&A using OpenAI, Qdrant Cloud, and Neon Serverless Postgres.

## Technical Context

<!--
  The following details are derived from the project constitution.
  Clarify or update as needed during planning.
-->

**Language/Version**: Python 3.11+, TypeScript (React/Docusaurus)
**Primary Dependencies**: FastAPI, Qdrant, Neon (psycopg2), OpenAI, Docusaurus
**Storage**: Neon Serverless Postgres, Qdrant Cloud
**Testing**: pytest, Vitest/React Testing Library
**Target Platform**: Web (Vercel/Netlify for frontend, preferred PaaS for backend)
**Project Type**: Web Application (Backend + Frontend)
**Performance Goals**: p95 query response <3s for `/ask` endpoint; ingestion of 100 markdown pages in <5 minutes.
**Constraints**: Must be embeddable in Docusaurus, must support user text selection for contextual Q&A, OpenAI generation model configurable, Semantic Chunking strategy for ingestion, Admin Credentials for /ingest endpoint.
**Scale/Scope**: Chatbot for a book with ~14 chapters and appendices.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Persona Alignment**: Does the plan align with the expert RAG engineer persona?
- [X] **Tech Stack**: Does the plan adhere to the defined technology stack (FastAPI, Neon, Qdrant, OpenAI, Docusaurus)?
- [X] **Dual-Mode Chatbot**: Does the plan address both global and contextual Q&A requirements?
- [X] **Modularity**: Is the architecture modular and specification-driven?

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot-system/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: The structure below is recommended based on the constitution.
  Update it with the concrete layout for this feature.
-->

```text
# Web application (frontend + backend)
rag-chatbot-api/ # FastAPI backend
├── src/
│   ├── models/
│   ├── services/
│   ├── api/
│   └── core/ # RAG pipeline logic
└── tests/

book-docusaurus-site/
├── src/
│   ├── components/
│   │   └── Chatbot/ # New React component for the chatbot
│   ├── theme/ # Potentially for chatbot styling
│   └── services/ # API client for the chatbot
└── ...
```

**Structure Decision**: The project follows a frontend/backend split. The backend is a new FastAPI application `rag-chatbot-api/` and the frontend is the existing Docusaurus site `book-docusaurus-site/` which will be modified to include the chatbot components.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| | | |