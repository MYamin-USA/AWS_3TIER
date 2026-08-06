FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt-get/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose internal port 8080 (bypassing default 8501)
EXPOSE 8080

# Command to run Streamlit on port 8080
CMD ["streamlit", "run", "aws_python.py", "--server.port=8080", "--server.address=0.0.0.0"]