FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY generate.py .

# ACI will override CMD/args if needed, but default is to run the script
CMD ["python", "generate.py"]
