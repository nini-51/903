# Utiliser une image Python de base
FROM python:3.9-slim

# Mettre en place le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY motd-api.py /app/motd-api.py

# Installer les dépendances
RUN pip install Flask

# Définir les variables d'environnement par défaut
ENV MESSAGE="Hello, world!"
ENV APP_PORT=8080

# Exposer le port sur lequel l'application écoute
EXPOSE $APP_PORT

# Commande pour exécuter l'application lorsque le conteneur démarre
CMD ["python", "motd-api.py"]
