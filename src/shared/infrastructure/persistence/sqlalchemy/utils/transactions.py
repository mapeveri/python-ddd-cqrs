from functools import update_wrapper, partial
from typing import Any

from dependency_injector.wiring import Provide

from src.shared.domain.unit_of_work import UnitOfWork


class Transactional:
    uow: UnitOfWork = Provide["unit_of_work"]

    def __init__(self, func: Any) -> None:
        update_wrapper(self, func)
        self.func = func

    def __get__(self, obj: Any, objtype: Any) -> partial:
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj: Any, *args: Any, **kwargs: Any) -> None:
        with self.uow():
            self.func(obj, *args, **kwargs)


transactional = Transactional
