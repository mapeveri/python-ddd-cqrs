import datetime
from abc import ABC

from src.shared.domain.value_objects.custom_uuid import Uuid


class DomainEvent(ABC):
    aggregate_id: str
    event_id: str
    occurred_on: str

    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self.event_id = Uuid.next()
        self.occurred_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def event_name() -> str:
        ...

    @classmethod
    def name(cls):
        return cls.__name__
