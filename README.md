# TP Docker - Serveur web Python

Dockerfile qui construit un serveur web Python basé sur l'image `python:3.13-slim`.
Le serveur web est le module intégré `http.server` de Python, qui sert `index.html` sur le port 9000.

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
