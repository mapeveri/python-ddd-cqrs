from typing import Protocol


class SendEmail(Protocol):
    def send(self, title: str, content: str) -> None:
        ...
