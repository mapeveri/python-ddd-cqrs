from flasgger import Swagger
from flask import Flask


def configure_swagger(app: Flask) -> None:
    app.config["SWAGGER"] = {"title": "Events V1 API DOCS", "doc_dir": "./docs/v1"}
    Swagger(app)
