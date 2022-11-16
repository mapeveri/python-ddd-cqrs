from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.shared.domain.unit_of_work import UnitOfWork
from src.shared.infrastructure.persistence.sqlalchemy.unit_of_work import SqlAlchemyUnitOfWorkItem


class SqlAlchemyUnitOfWork(UnitOfWork):
    db: SQLAlchemy = Provide["db"]

    def __call__(self) -> SqlAlchemyUnitOfWorkItem:
        return SqlAlchemyUnitOfWorkItem(self.db)
