from dataclasses import dataclass
from typing import Optional

from src.shared.domain.bus.command.command import Command


@dataclass(frozen=True)
class CreateEventResponseCommand(Command):
    id: str
    provider_id: int
    mode: str
    provider_organizer_company_id: Optional[int]
    title: str
    start_date: str
    end_date: str
    sell_from: str
    sell_to: str
    sold_out: bool
    zones: list
