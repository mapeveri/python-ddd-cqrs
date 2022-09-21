from dataclasses import dataclass

from src.shared.domain.value_objects.custom_uuid import Uuid


@dataclass
class EventId(Uuid):
    def __init__(self, id: str):
        super(EventId, self).__init__(id)

    def __hash__(self):
        return hash(self.id)
