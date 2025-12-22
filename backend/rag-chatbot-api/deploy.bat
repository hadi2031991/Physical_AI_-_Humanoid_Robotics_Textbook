@echo off
REM deploy.bat - Windows deployment script for RAG Chatbot

echo Starting RAG Chatbot deployment...

REM Check if .env file exists
if not exist ".env" (
    echo Please create a .env file with your environment variables first!
    echo Example .env file:
    echo OPENAI_API_KEY=your_openai_api_key_here
    echo NEON_DATABASE_URL=your_database_url_here
    exit /b 1
)

REM Build and start the services
echo Building and starting services...
docker-compose up -d --build

echo Waiting for services to start...
timeout /t 10

REM Check if the service is running
docker-compose ps | findstr "Up" >nul
if %errorlevel% == 0 (
    echo RAG Chatbot is now running!
    echo Access the application at http://localhost:8000
    echo API documentation at http://localhost:8000/docs
) else (
    echo There was an issue starting the services. Check logs with 'docker-compose logs'
    exit /b 1
)

echo Deployment completed successfully!