from dataclasses import dataclass
from typing import List

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.zone import Zone
from src.marketplace.event.domain.zone_repository import ZoneRepository


@dataclass
class SqlAlchemyZoneRepository(ZoneRepository):
    db: SQLAlchemy = Provide["db"]

    def zones_by_event_id(self, event_id: EventId) -> List[Zone]:
        return self.db.session.query(Zone).filter(Zone.event_id == event_id.id)
