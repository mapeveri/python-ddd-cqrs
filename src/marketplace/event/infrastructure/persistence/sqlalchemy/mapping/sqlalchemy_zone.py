from sqlalchemy import Table, Column, String, Integer, Boolean

from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.event_id_decorator import EventIdDecorator
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.zone_id_decorator import ZoneIdDecorator
from src.shared.infrastructure.persistence.sqlalchemy.decorators.price_decorator import PriceDecorator
from src.shared.infrastructure.persistence.sqlalchemy.registry import mapper_registry


zone_table = Table(
    'zone',
    mapper_registry.metadata,
    Column('id', ZoneIdDecorator, primary_key=True),
    Column('provider_zone_id', Integer, nullable=False),
    Column('capacity', Integer, nullable=False),
    Column('price', PriceDecorator, nullable=False),
    Column('name', String(500), nullable=False),
    Column('numbered', Boolean, nullable=False, default=False),
    Column("event_id", EventIdDecorator, nullable=False)
)

