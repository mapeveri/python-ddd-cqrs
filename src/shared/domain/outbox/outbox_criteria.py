from dataclasses import dataclass


@dataclass
class OutboxCriteria:
    limit: int = 200
    order_by: str = "created_at asc"
