# TP Docker - Serveur web Python

Dockerfile qui construit un serveur web Python basé sur l'image `python:3.13-slim`.

## Contenu

- `Dockerfile` : construction de l'image
- `app.py` : serveur web (bibliothèque standard Python, port 9000)
- `www/index.html` : page d'accueil
- `/api/info` : renvoie le nom du conteneur, la version de Python et l'heure en JSON

## Build de l'image

Dans le dossier du Dockerfile :

```bash
docker build -t image_name .
```

## Lancer un conteneur

```bash
docker run -it --rm \
    --name="my_webserver" \
    -p 9000:9000 \
    image_name
```

Puis ouvrir http://localhost:9000
