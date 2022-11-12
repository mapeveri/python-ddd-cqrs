from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Mode:
    mode_value: str

    ONLINE: str = "online"
    OFFLINE: str = "offline"

    def value(self) -> str:
        return self.mode_value

    @classmethod
    def create_online(cls) -> Mode:
        return cls(cls.ONLINE)
