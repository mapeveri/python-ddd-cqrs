from dataclasses import dataclass

from src.marketplace.event.domain.event import Event
from src.marketplace.event.domain.event_repository import EventRepository
from src.marketplace.event.domain.exceptions.event_not_found_exception import EventNotFoundException


@dataclass
class EventFinderByProviderId:
    def __init__(self, event_repository: EventRepository) -> None:
        self.__event_repository = event_repository

    def by_provider_id(self, provider_id: int) -> Event:
        event = self.__event_repository.find_by_provider_id(provider_id)
        if not event:
            raise EventNotFoundException(provider_id)

        return event
