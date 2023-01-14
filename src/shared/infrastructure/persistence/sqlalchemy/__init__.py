import os
from pydoc import locate
from typing import List

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapper as sqlalchemy_mapper, clear_mappers


def configure_database(flask_app: Flask) -> SQLAlchemy:
    db = SQLAlchemy(flask_app, session_options={"autocommit": True})
    flask_app.db = db
    Migrate(flask_app, db, os.path.join(os.path.dirname(flask_app.root_path), "migrations"))

    mappers: List[str] = [
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.event_mapper.EventMapper",
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.zone_mapper.ZoneMapper",
        "src.marketplace.event.infrastructure.persistence.sqlalchemy.mapping.event_file_mapper.EventFileMapper",
        "src.shared.infrastructure.persistence.sqlalchemy.mapping.outbox_mapper.OutboxMapper",
    ]

    clear_mappers()
    for mapper_class in mappers:
        # noinspection PyCallingNonCallable
        entity_mapper = locate(mapper_class)(db)
        sqlalchemy_mapper(entity_mapper.entity(), entity_mapper.table(), **entity_mapper.extra_config())

    return db
