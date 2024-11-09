FROM python:3.11-slim

WORKDIR /app

# Install netcat and clean up in a single layer
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Fix line endings, set permissions, and remove dependencies not needed at runtime
RUN sed -i 's/\r$//g' wait-for-it.sh && \
    chmod +x wait-for-it.sh

CMD ["sh", "./wait-for-it.sh", "db", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
