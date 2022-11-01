from typing import Type

from sqlalchemy import Table, Column, String, Integer, Boolean

from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.event_id_decorator import EventIdDecorator
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.zone_id_decorator import ZoneIdDecorator
from src.shared.infrastructure.persistence.sqlalchemy.decorators.price_decorator import PriceDecorator
from src.shared.infrastructure.persistence.sqlalchemy.utils.mapper import Mapper


class ZoneMapper(Mapper):
    def _create_table(self) -> Table:
        return self._db_instance.Table(
            "zone",
            Column('id', ZoneIdDecorator, primary_key=True),
            Column('provider_zone_id', Integer, nullable=False),
            Column('capacity', Integer, nullable=False),
            Column('price', PriceDecorator, nullable=False),
            Column('name', String(500), nullable=False),
            Column('numbered', Boolean, nullable=False, default=False),
            Column("event_id", EventIdDecorator, nullable=False)
        )

    def entity(self) -> Type:
        return Zone
