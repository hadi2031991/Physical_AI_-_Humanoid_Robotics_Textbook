# Data Model: Textbook Content Structure

The textbook's content adheres to a hierarchical structure, designed for clear organization and modularity within the Docusaurus framework.

## Entities

### Book
- **Description**: The complete academic textbook on Physical AI & Humanoid Robotics.
- **Attributes**:
    - `title`: String (e.g., "Physical AI & Humanoid Robotics Textbook")
    - `parts`: List of Part entities
    - `appendices`: List of Appendix entities
    - `configuration`: Docusaurus configuration settings (e.g., `docusaurus.config.js`, `sidebars.js`)
    - `deployment_workflow`: GitHub Actions workflow for deployment

### Part
- **Description**: A major thematic section of the book, grouping related chapters.
- **Attributes**:
    - `name`: String (e.g., "Foundations of Physical AI")
    - `chapters`: List of Chapter entities
- **Relationship**: Contains Chapters.

### Chapter
- **Description**: A self-contained educational unit.
- **Attributes**:
    - `title`: String (e.g., "Introduction to Physical AI")
    - `slug`: String (URL-friendly identifier)
    - `content`: Markdown text (includes objectives, concepts, examples, diagrams, summary)
    - `exercises`: Markdown text or structured data for practice questions
- **Relationship**: Belongs to a Part.

### Appendix
- **Description**: Supplementary material providing additional depth or reference.
- **Attributes**:
    - `name`: String (e.g., "Math Fundamentals")
    - `slug`: String (URL-friendly identifier)
    - `content`: Markdown text
- **Relationship**: Belongs to the Book.

## Relationships

- **Book to Parts**: One-to-many. A Book contains multiple Parts.
- **Part to Chapters**: One-to-many. A Part contains multiple Chapters.
- **Book to Appendices**: One-to-many. A Book contains multiple Appendices.

## Structure Representation

The `spec.yaml` will explicitly define this hierarchical structure, listing all parts, chapters, and appendices, serving as the blueprint for content generation and Docusaurus navigation.
