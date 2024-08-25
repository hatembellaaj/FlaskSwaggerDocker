# Utilisation de l'image de base python:3.9-slim
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de l'application dans le conteneur
COPY . /app

# Installation des packages Python à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour l'application Flask
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python", "app.py"]
