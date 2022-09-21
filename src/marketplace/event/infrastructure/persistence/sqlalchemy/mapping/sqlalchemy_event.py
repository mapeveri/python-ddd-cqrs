from sqlalchemy import Table, Column, String, Integer, DateTime, Boolean

from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.event_id_decorator import EventIdDecorator
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.mode_decorator import ModeDecorator
from src.shared.infrastructure.persistence.sqlalchemy.registry import mapper_registry


event_table = Table(
    'event',
    mapper_registry.metadata,
    Column('id', EventIdDecorator, primary_key=True),
    Column('provider_id', Integer, unique=True, nullable=False),
    Column('mode', ModeDecorator, nullable=False),
    Column('title', String(500), nullable=False),
    Column('provider_organizer_company_id', Integer, nullable=True),
    Column('start_date', DateTime, nullable=False),
    Column('end_date', DateTime, nullable=False),
    Column('sell_from', DateTime, nullable=False),
    Column('sell_to', DateTime, nullable=False),
    Column('sold_out', Boolean, nullable=False, default=False)
)


