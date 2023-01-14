from __future__ import annotations

from dataclasses import dataclass

from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.file_id import FileId


@dataclass
class File:
    id: FileId
    file: str
    event_id: EventId

    @classmethod
    def create(
        cls,
        file_id: FileId,
        file: str,
        event_id: EventId,
    ) -> File:
        return cls(file_id, file, event_id)
