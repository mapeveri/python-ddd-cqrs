from __future__ import annotations

import datetime
from abc import ABC
from typing import Dict, Any, Optional

from src.shared.domain.value_objects.custom_uuid import Uuid


class DomainEvent(ABC):
    aggregate_id: str
    event_id: str
    occurred_on: str

    def __init__(self, aggregate_id: str, event_id: Optional[str] = None, occurred_on: Optional[str] = None) -> None:
        self.aggregate_id = aggregate_id
        self.event_id = Uuid.next() if event_id is None else event_id
        self.occurred_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if occurred_on is None else occurred_on

    @classmethod
    def from_primitives(cls, payload: Dict[Any, Any]) -> DomainEvent:
        ...

    @staticmethod
    def event_name() -> str:
        ...

    @staticmethod
    def aggregate_type() -> str:
        ...

    @classmethod
    def name(cls) -> str:
        return cls.__name__
