from functools import update_wrapper, partial
from typing import Any

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy


class Transactional:
    db: SQLAlchemy = Provide["db"]

    def __init__(self, func: Any) -> None:
        update_wrapper(self, func)
        self.func = func

    def __get__(self, obj: Any, objtype: Any) -> partial:
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj: Any, *args: Any, **kwargs: Any) -> None:
        try:
            self.db.session.begin()
            self.func(obj, *args, **kwargs)
            self.db.session.commit()
        except Exception as e:
            print("Exception: Transactional")
            self.db.session.rollback()
            raise Exception(e)


transactional = Transactional
