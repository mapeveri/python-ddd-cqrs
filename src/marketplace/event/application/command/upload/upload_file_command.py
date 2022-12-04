from dataclasses import dataclass
from typing import Optional

from src.shared.domain.bus.command.command import Command


@dataclass(frozen=True)
class UploadFileCommand(Command):
    content: bytes
    path: str
    chunk_range: Optional[int]
    chunk: bool = False
