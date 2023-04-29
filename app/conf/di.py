from celery import Celery
from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from redis import Redis

from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.di.modules import MODULES


def configure_di_container(
        app: Flask,
        db: SQLAlchemy,
        es: Elasticsearch,
        celery: Celery,
        mail: Mail,
        redis: Redis
) -> DI:
    container = DI(app=app, db=db, es=es, celery=celery, mail=mail, redis=redis)
    container.wire(modules=MODULES)

    return container
