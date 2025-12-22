#!/bin/bash
# deploy.sh - Simple deployment script for RAG Chatbot

set -e

echo "Starting RAG Chatbot deployment..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Please create a .env file with your environment variables first!"
    echo "Example .env file:"
    echo "OPENAI_API_KEY=your_openai_api_key_here"
    echo "NEON_DATABASE_URL=your_database_url_here"
    exit 1
fi

# Build and start the services
echo "Building and starting services..."
docker-compose up -d --build

echo "Waiting for services to start..."
sleep 10

# Check if the service is running
if docker-compose ps | grep -q "Up"; then
    echo "RAG Chatbot is now running!"
    echo "Access the application at http://localhost:8000"
    echo "API documentation at http://localhost:8000/docs"
else
    echo "There was an issue starting the services. Check logs with 'docker-compose logs'"
    exit 1
fi

echo "Deployment completed successfully!"