from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass

from src.shared.domain.value_objects.outbox_id import OutboxId


@dataclass
class Outbox:
    id: OutboxId
    aggregate_type: str
    aggregate_id: str
    type: str
    payload: str
    created_at: datetime

    @classmethod
    def create(
        cls,
        id: OutboxId,
        aggregate_type: str,
        aggregate_id: str,
        type: str,
        payload: str,
    ) -> Outbox:
        return cls(
            id,
            aggregate_type,
            aggregate_id,
            type,
            payload,
            datetime.utcnow(),
        )
