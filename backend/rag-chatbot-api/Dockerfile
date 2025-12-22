FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

# Download model at build time to avoid downloading each time
RUN python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; \
    from sentence_transformers import SentenceTransformer; \
    AutoTokenizer.from_pretrained('microsoft/DialoGPT-small'); \
    AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-small'); \
    SentenceTransformer('all-MiniLM-L6-v2');"

CMD ["python", "app.py"]