from dataclasses import dataclass

from src.shared.domain.value_objects.custom_uuid import Uuid


@dataclass
class ZoneId(Uuid):
    def __init__(self, id: str) -> None:
        super(ZoneId, self).__init__(id)

    def __hash__(self) -> int:
        return hash(self.id)
