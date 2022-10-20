from datetime import datetime

from sqlalchemy import Table, Column, String, Text, DateTime
from sqlalchemy.orm import registry

from src.shared.domain.outbox import Outbox
from src.shared.infrastructure.persistence.sqlalchemy.decorators.outbox_id_decorator import OutboxIdDecorator

mapper_registry = registry()

outbox_table = Table(
    'outbox',
    mapper_registry.metadata,
    Column('id', OutboxIdDecorator, primary_key=True),
    Column('aggregate_type', String(50), nullable=False),
    Column('aggregate_id', String(255), nullable=False),
    Column('type', String(255), nullable=False),
    Column('payload', Text, nullable=False),
    Column('created_at', DateTime, nullable=False, default=datetime.utcnow),
)


def mapper_shared_context_tables():
    mapper_registry.map_imperatively(Outbox, outbox_table)
