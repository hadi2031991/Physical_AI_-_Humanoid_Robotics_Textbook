---
id: 09
title: List Available NPM Scripts
stage: misc
date: 2025-12-09
surface: agent
model: gemini
feature: textbook-content
branch: 001-textbook-content
user: [user]
command: npm run
labels: ["npm", "scripts", "docusaurus"]
links:
  spec: specs/001-textbook-content/spec.md
  plan: specs/001-textbook-content/plan.md
  tasks: specs/001-textbook-content/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - book-docusaurus-site/package.json
tests:
 - "N/A"
---

## Prompt

npm run

## Response snapshot

Successfully listed the available npm scripts for the Docusaurus project.

## Outcome

- ✅ Impact: Low. Provided requested information about available npm scripts.
- 🧪 Tests: N/A. No code changes or tests were run.
- 📁 Files: N/A. No files were modified.
- 🔁 Next prompts: The user can now choose to run any of the listed npm scripts.
- 🧠 Reflection: The request was straightforward information retrieval.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
