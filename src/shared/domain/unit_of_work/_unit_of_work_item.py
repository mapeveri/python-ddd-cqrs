from __future__ import annotations

from abc import ABC, abstractmethod
from types import TracebackType
from typing import ContextManager, Optional, Type


class UnitOfWorkItem(ContextManager, ABC):
    @abstractmethod
    def _start(self) -> None:
        ...

    @abstractmethod
    def _complete(self) -> None:
        ...

    @abstractmethod
    def _discard(self) -> None:
        ...

    def __enter__(self) -> UnitOfWorkItem:
        self._start()
        return self

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> None:
        if __exc_type is not None:
            self._discard()
            return

        try:
            self._complete()
        except Exception as exception:
            self._discard()
            raise exception
