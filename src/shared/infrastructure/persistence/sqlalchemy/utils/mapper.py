from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy


class Mapper(ABC):
    def __init__(self, db_instance: SQLAlchemy) -> None:
        self._db_instance = db_instance
        self._table = None

    def table(self) -> Table:
        if self._table is None:
            self._table = self._create_table()

        return self._table

    @abstractmethod
    def _create_table(self) -> Table:
        pass

    @abstractmethod
    def entity(self) -> Type:
        pass

    def extra_config(self) -> dict:
        return {}
