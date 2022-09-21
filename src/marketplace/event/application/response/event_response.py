from dataclasses import dataclass


@dataclass(frozen=True)
class EventResponse:
    id: str
    title: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    min_price: float
    max_price: float
