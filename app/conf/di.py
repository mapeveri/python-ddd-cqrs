from celery import Celery
from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.di.modules import MODULES


def configure_di_container(app: Flask, db: SQLAlchemy, es: Elasticsearch, celery: Celery, mail: Mail) -> DI:
    container = DI(app=app, db=db, es=es, celery=celery, mail=mail)
    container.wire(modules=MODULES)

    return container
