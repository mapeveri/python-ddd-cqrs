from dataclasses import dataclass

from src.shared.domain.value_objects.outbox_id import OutboxId


@dataclass
class Outbox:
    id: OutboxId
    aggregate_type: str
    aggregate_id: str
    type: str
    payload: str
