from dataclasses import dataclass

from src.shared.domain.value_objects.custom_uuid import Uuid


@dataclass
class FileId(Uuid):
    def __init__(self, id: str) -> None:
        super(FileId, self).__init__(id)

    def __hash__(self) -> int:
        return hash(self.id)
