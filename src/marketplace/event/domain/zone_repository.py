import abc
from typing import List, Protocol

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.zone import Zone


class ZoneRepository(Protocol):
    @abc.abstractmethod
    def zones_by_event_id(self, event_id: EventId) -> List[Zone]:
        ...
