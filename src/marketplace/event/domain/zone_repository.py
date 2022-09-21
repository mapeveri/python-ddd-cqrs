import abc
from typing import List

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.zone import Zone


class ZoneRepository(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def zones_by_event_id(self, event_id: EventId) -> List[Zone]:
        ...
