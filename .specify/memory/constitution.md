<!--
---
version_change: "1.0.0 -> 2.0.0"
modified_principles:
  - "Principle I: Adherence to the Expert Persona"
  - "Principle II: Defined Technology Stack"
  - "Principle III: Dual-Mode RAG Chatbot"
  - "Principle IV: Spec-Driven and Modular Development"
added_sections: []
removed_sections:
  - "I. Accuracy, Clarity, and Academic Tone"
  - "II. Future-Oriented Perspective"
  - "III. Modular Chapter Organization"
templates_updated:
  - "`.specify/memory/constitution.md` (✅ updated)"
  - "`.specify/templates/plan-template.md` (✅ updated)"
  - "`.specify/templates/spec-template.md` (✅ updated)"
  - "`.specify/templates/tasks-template.md` (✅ updated)"
todos: []
---
-->
# AI Book Constitution

## Core Principles

### I. Adherence to the Expert Persona
All development, architectural decisions, and communication must align with the persona of an expert full-stack engineer specializing in Retrieval-Augmented Generation (RAG), OpenAI Agents, FastAPI, Neon Serverless Postgres, and Qdrant Cloud vector search. This ensures the project benefits from specialized expertise and follows industry best practices for the chosen technologies.

### II. Defined Technology Stack
The project will exclusively use the following technologies for its core functionality:
- **Backend API:** FastAPI
- **Vector Search:** Qdrant Cloud
- **Database:** Neon Serverless Postgres
- **AI/LLM:** OpenAI Platform (Agents, Embeddings)
- **Frontend Host:** Docusaurus

This standardization ensures maintainability, interoperability, and focuses development effort.

### III. Dual-Mode RAG Chatbot
The primary deliverable is a Retrieval-Augmented Generation (RAG) chatbot embedded in the Docusaurus site. It MUST support two modes of operation:
1.  **Global Q&A:** Answers questions based on the entire book's content.
2.  **Contextual Q&A:** Answers questions based only on user-selected text from the website.

This addresses the core functional requirement of providing both broad and specific information retrieval to the user.

### IV. Spec-Driven and Modular Development
Development must follow a specification-driven approach. Features will be broken down into modular, testable components. The backend (FastAPI), frontend (Docusaurus/React), and data pipelines (RAG) should be decoupled to the greatest extent possible to promote clarity, reduce complexity, and facilitate parallel development and testing.

## Project Scope

- **Backend:** Implement a FastAPI service for handling chatbot queries, including RAG pipeline orchestration.
- **Frontend:** Develop a React component to be embedded in Docusaurus, providing the chatbot UI and handling user text selection.
- **RAG Pipeline:** Build the data ingestion and retrieval pipeline to populate and query Qdrant from the book's content.
- **Integration:** Fully integrate the frontend component with the backend API.
- **Deployment:** Configure the backend and frontend for a production environment.

## Governance

This constitution guides the project's development. All contributions must align with these principles and constraints. Amendments require team consensus and documentation.

**Version**: 2.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-10
