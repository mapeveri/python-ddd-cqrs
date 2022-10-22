from functools import update_wrapper, partial

from dependency_injector.wiring import inject, Provide
from flask_sqlalchemy import SQLAlchemy


class Transactional:
    db: SQLAlchemy = Provide['db']

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj, *args, **kwargs):
        try:
            self.db.session.begin()
            self.func(obj, *args, **kwargs)
            self.db.session.commit()
        except Exception as e:
            print("Exception: Transactional")
            self.db.session.rollback()
            raise Exception(e)


transactional = Transactional

