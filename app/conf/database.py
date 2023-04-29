import os
from pydoc import locate
from typing import List

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import registry as sqlalchemy_registry, clear_mappers


def configure_database(app: Flask) -> SQLAlchemy:
    db = SQLAlchemy(app)
    app.db = db
    Migrate(app, db, os.path.join(os.path.dirname(app.root_path), "migrations"))

    mappers: List[str] = [
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.event_mapper.EventMapper",
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.event_zone_mapper.EventZoneMapper",
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.event_file_mapper.EventFileMapper",
        "src.shared.infrastructure.persistence.sqlalchemy.mapping.outbox_mapper.OutboxMapper",
    ]

    clear_mappers()
    for mapper_class in mappers:
        # noinspection PyCallingNonCallable
        entity_mapper = locate(mapper_class)(db)
        sqlalchemy_registry().map_imperatively(
            entity_mapper.entity(),
            entity_mapper.table(),
            **entity_mapper.extra_config(),
        )

    return db
