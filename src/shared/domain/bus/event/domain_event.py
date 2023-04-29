from __future__ import annotations

import datetime
from abc import ABC
from typing import Dict, Any
from uuid import NAMESPACE_DNS, uuid5


class DomainEvent(ABC):
    aggregate_id: str
    event_id: str
    occurred_on: str

    def __init__(self, aggregate_id: str) -> None:
        self.aggregate_id = aggregate_id
        self.event_id = str(uuid5(NAMESPACE_DNS, aggregate_id))
        self.occurred_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
