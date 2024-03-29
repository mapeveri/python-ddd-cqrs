from dataclasses import dataclass
from typing import Optional

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.value_objects.event_id import EventId


@dataclass
class SqlAlchemyEventRepository(EventRepository):
    db: SQLAlchemy = Provide["db"]

    def find_by_id(self, event_id: EventId) -> Optional[Event]:
        return self.db.session.query(Event).filter_by(id=event_id).one_or_none()

    def find_by_provider_id(self, provider_id: int) -> Optional[Event]:
        return self.db.session.query(Event).filter_by(provider_id=provider_id).one_or_none()

    def save(self, event: Event) -> None:
        self.db.session.add(event)

        if event.zones:
            self.db.session.add_all(event.zones)
