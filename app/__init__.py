from elasticsearch import Elasticsearch
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_mail import Mail

from src.shared.infrastructure import shared_blueprint
from src.shared.infrastructure.bus.register import configure_buses
from src.shared.infrastructure.celery.configuration import configure_celery
from src.marketplace.event.infrastructure import event_blueprint
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.di.modules import MODULES
from src.shared.infrastructure.persistence.sqlalchemy import configure_database


def flask_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('app.conf.config')
    app.config['SWAGGER'] = {
        'title': 'Events V1 API DOCS',
        'doc_dir': './docs/v1'
    }
    Swagger(app)
    CORS(app, resource={r'/*': {'origins': app.config['ALLOWED_CLIENT_URL']}})
    mail = Mail(app)

    celery = configure_celery(app)
    app.celery = celery

    db = configure_database(app)
    es = Elasticsearch(app.config['ELASTICSEARCH_URL'])

    container = DI(app=app, db=db, es=es, celery=celery, mail=mail)
    container.wire(modules=MODULES)
    app.container = container

    configure_buses()

    app.register_blueprint(event_blueprint.blueprint, url_prefix='/api/v1')
    app.register_blueprint(shared_blueprint.blueprint)

    return app
