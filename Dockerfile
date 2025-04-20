FROM python:3.9-slim
WORKDIR /app

# Copie des dépendances d'abord pour mieux utiliser le cache Docker
COPY requirements.txt .
COPY setup.py .

# Installation des dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -e .

# Copie du code source
COPY app ./app
COPY src ./src

EXPOSE 8000

# Si vous utilisez FastAPI/uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]