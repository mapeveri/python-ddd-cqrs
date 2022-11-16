from __future__ import annotations

from abc import ABC, abstractmethod

from src.shared.domain.unit_of_work import UnitOfWorkItem


class UnitOfWork(ABC):
    @abstractmethod
    def __call__(self) -> UnitOfWorkItem:
        pass
