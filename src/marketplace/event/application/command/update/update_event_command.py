from dataclasses import dataclass
from typing import Optional

from src.shared.domain.bus.command.command import Command


@dataclass(frozen=True)
class UpdateEventCommand(Command):
    provider_id: int
    provider_organizer_company_id: Optional[int]
    title: str
    start_date: str
    end_date: str
    sell_from: str
    sell_to: str
    sold_out: bool
    zones: list
