"""Serveur web minimal en Python (bibliothèque standard uniquement)."""
import json
import os
import platform
import socket
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 9000))
WEB_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_ROOT, **kwargs)

    def do_GET(self):
        # Petite API qui renvoie des infos sur le conteneur
        if self.path == "/api/info":
            data = {
                "hostname": socket.gethostname(),
                "python": platform.python_version(),
                "time": datetime.now().isoformat(timespec="seconds"),
            }
            body = json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


if __name__ == "__main__":
    print(f"Serveur web démarré sur le port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
