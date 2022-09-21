from elasticsearch import Elasticsearch
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.infrastructure.persistence.sqlalchemy.registry.registry import mapper_event_context_tables
from src.shared.infrastructure.celery.configuration import configure_celery
from src.marketplace.event.infrastructure.ui.rest import views as events_views
from src.shared.infrastructure.di.container import DI
from src.shared.infrastructure.bus.register import register_commands, register_queries, register_events

app = Flask(__name__)
app.config.from_object('apps.api.conf.config')

celery = configure_celery(app)
app.celery = celery

db = SQLAlchemy(app)
app.db = db
Migrate(app, db)

es = Elasticsearch(app.config['ELASTICSEARCH_URL'])

mapper_event_context_tables()

container = DI(app=app, db=db, es=es)
container.wire(
    modules=[
        'src.shared.infrastructure.api_controller',
        'src.shared.infrastructure.bus.register',
        'src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_event_repository',
        'src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_zone_repository',
        'src.marketplace.event.infrastructure.persistence.elasticsearch.repository'
        '.elasticsearch_event_response_repository',
        'src.marketplace.event.infrastructure.services.events_provider.process_events_provider'
    ],
)
app.container = container

register_commands()
register_queries()
register_events()

app.register_blueprint(events_views.blueprint)
