# Dockerfile
FROM python:3.8-slim

WORKDIR /app

# Copia e installa le dipendenze
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia il codice sorgente
COPY . .

# Comando di default: esegue lo script di training
CMD ["python", "src/train_model.py"]
