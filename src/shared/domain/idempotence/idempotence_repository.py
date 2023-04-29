from abc import ABC, abstractmethod
from typing import Any, Optional


class IdempotenceRepository(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        ...

    @abstractmethod
    def set(self, key: str, value: Any) -> None:
        ...
