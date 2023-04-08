from flask import Flask

from app.conf.buses import configure_buses
from app.conf.celery import configure_celery
from app.conf.cors import configure_cors
from app.conf.database import configure_database
from app.conf.di import configure_di_container
from app.conf.elasticsearch import configure_elasticsearch
from app.conf.error_handlers import configure as configure_errors
from app.conf.mail import configure_mail
from app.conf.swagger import configure_swagger
from app.marketplace_app import MarketplaceApp


def flask_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.conf.config")
    marketplace_instance: MarketplaceApp = MarketplaceApp(app)

    configure_swagger(app)
    configure_cors(app)
    mail = configure_mail(app)

    celery = configure_celery(app)
    app.celery = celery

    db = configure_database(app)
    es = configure_elasticsearch(app)

    container = configure_di_container(app, db, es, celery, mail)
    app.container = container

    configure_errors(app)
    configure_buses()

    marketplace_instance.setup_app()

    return app
