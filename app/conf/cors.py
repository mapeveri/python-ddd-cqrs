from flask import Flask
from flask_cors import CORS


def configure_cors(app: Flask) -> None:
    CORS(app, resource={r"/*": {"origins": app.config["ALLOWED_CLIENT_URL"]}})
