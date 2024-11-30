FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exposer le port 5001 
EXPOSE 5001

# Commande pour exécuter l'application
CMD ["python", "app.py"]
