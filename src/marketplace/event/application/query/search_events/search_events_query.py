from dataclasses import dataclass
from typing import Optional

from src.shared.domain.bus.query.query import Query


@dataclass(frozen=True)
class SearchEventsQuery(Query):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
