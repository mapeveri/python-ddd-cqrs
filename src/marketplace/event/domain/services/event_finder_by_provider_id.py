from dataclasses import dataclass

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.exceptions import EventNotFound


@dataclass
class EventFinderByProviderId:
    repository: EventRepository

    def __call__(self, provider_id: int) -> Event:
        event = self.repository.find_by_provider_id(provider_id)
        if not event:
            raise EventNotFound("Event not found")

        return event
