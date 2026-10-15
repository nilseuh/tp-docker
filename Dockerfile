# Image de base : Python 3.13 version allégée
FROM python:3.13-slim

# Pas de fichiers .pyc, logs affichés directement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=9000

# Dossier de travail dans le conteneur
WORKDIR /app

# Copie du code du serveur web
COPY app.py .
COPY www/ ./www/

# Utilisateur non-root pour exécuter le serveur
RUN useradd --create-home --uid 1000 appuser
USER appuser

# Port exposé par le serveur web
EXPOSE 9000

# Lancement du serveur
CMD ["python", "app.py"]
