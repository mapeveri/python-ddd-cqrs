from elasticsearch import Elasticsearch
from flask import Flask
from flask_cors import CORS, cross_origin
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from src.shared.infrastructure import shared_blueprint
from src.shared.infrastructure.bus.register import configure_buses
from src.shared.infrastructure.celery.configuration import configure_celery
from src.marketplace.event.infrastructure import event_blueprint
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.persistence.sqlalchemy import configure_database


def flask_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('app.conf.config')

    CORS(app, resource={
        r'/*': {
            'origins': app.config['ALLOWED_CLIENT_URL']
        }
    })

    celery = configure_celery(app)
    app.celery = celery

    db = configure_database(app)

    es = Elasticsearch(app.config['ELASTICSEARCH_URL'])

    container = DI(app=app, db=db, es=es, celery=celery)
    container.wire(
        modules=[
            'src.shared.infrastructure.api_controller',
            'src.shared.infrastructure.bus.event.mapping',
            'src.shared.infrastructure.bus.register',
            'src.shared.infrastructure.persistence.sqlalchemy.unit_of_work._sql_alchemy_unit_of_work',
            'src.shared.infrastructure.persistence.sqlalchemy.utils.transactions',
            'src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_event_repository',
            'src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_zone_repository',
            'src.marketplace.event.infrastructure.persistence.elasticsearch.repository'
            '.elasticsearch_event_response_repository',
            'src.marketplace.event.infrastructure.services.events_provider.process_events_provider',
            'src.shared.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_outbox_repository',
            'src.shared.infrastructure.console.commands.publish_domain_events_cli'
        ],
    )
    app.container = container

    configure_buses()

    app.register_blueprint(event_blueprint.blueprint)
    app.register_blueprint(shared_blueprint.blueprint)

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    return app
