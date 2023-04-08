from elasticsearch import Elasticsearch
from flask import Flask


def configure_elasticsearch(app: Flask) -> Elasticsearch:
    return Elasticsearch(app.config["ELASTICSEARCH_URL"])
