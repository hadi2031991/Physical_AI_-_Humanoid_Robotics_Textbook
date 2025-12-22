# RAG Chatbot Deployment Guide (Hugging Face Version)

## Prerequisites

- Docker and Docker Compose installed
- (Optional) PostgreSQL database
- Sufficient system resources to run Hugging Face models

## Environment Setup

1. Create a `.env` file in the project root:

```bash
HF_MODEL_NAME=microsoft/DialoGPT-small
NEON_DATABASE_URL=postgresql+asyncpg://username:password@ep-xxxx.us-east-1.aws.neon.tech/dbname
```

For local development, you can use the default PostgreSQL service in docker-compose.
The default model (DialoGPT-small) is used if HF_MODEL_NAME is not specified.

## Deployment Options

### Option 1: Using Docker Compose (Recommended for development)

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>/backend/rag-chatbot-api

# Create .env file with your settings
cp .env.example .env
# Edit .env to configure your settings

# Start the services
docker-compose up -d
```

The application will be available at `http://localhost:8000`

### Option 2: Production Deployment

For production, use the following docker-compose.prod.yml:

```yaml
version: '3.8'

services:
  rag-chatbot:
    build: .
    ports:
      - "80:8000"
    environment:
      - HF_MODEL_NAME=${HF_MODEL_NAME}
      - NEON_DATABASE_URL=${NEON_DATABASE_URL}
    volumes:
      - static_volume:/app/static
    depends_on:
      - db
    restart: unless-stopped
    networks:
      - rag_network

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: rag_chatbot
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secure_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    restart: unless-stopped
    networks:
      - rag_network

volumes:
  postgres_data:
  static_volume:

networks:
  rag_network:
    driver: bridge
```

## Configuration

### Database Configuration

The application supports both PostgreSQL and SQLite for development:

- For production: Use PostgreSQL with NEON_DATABASE_URL
- For development: Uses SQLite in-memory database if no PostgreSQL URL is provided

### Environment Variables

- `HF_MODEL_NAME`: Hugging Face model name (default: "microsoft/DialoGPT-small")
- `NEON_DATABASE_URL`: PostgreSQL connection string (optional, defaults to SQLite)
- `ENVIRONMENT`: Set to 'production' to enable production features

### Recommended Models

You can use any of these models with this RAG system:

- `microsoft/DialoGPT-small` - Lightweight conversational model
- `microsoft/DialoGPT-medium` - Better quality, larger model
- `gpt2` - General purpose model
- `distilgpt2` - Faster, smaller GPT-2 variant

## API Endpoints

- `GET /health`: Health check
- `POST /documents`: Upload documents (PDF, DOCX, TXT)
- `POST /chat`: Chat with the RAG model
- `GET /conversations`: List all conversations
- `GET /conversations/{id}`: Get specific conversation

## Scaling

For production scaling:

1. Use a production-grade PostgreSQL service
2. Implement Redis for caching
3. Add a load balancer
4. Use Docker Swarm or Kubernetes for orchestration
5. Consider GPU acceleration for faster model inference

## Security

- Never commit sensitive data to version control
- Use HTTPS in production
- Implement authentication for document upload
- Set up proper firewall rules

## Monitoring

The application logs to standard output, which can be captured by your container orchestration platform. For production, consider implementing structured logging and monitoring with tools like:

- Prometheus + Grafana
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Cloud monitoring services