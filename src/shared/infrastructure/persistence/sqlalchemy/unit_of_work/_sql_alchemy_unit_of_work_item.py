from typing import Optional

from flask_sqlalchemy import SignallingSession, SQLAlchemy
from sqlalchemy.orm import SessionTransaction

from src.shared.domain.unit_of_work import UnitOfWorkItem
from src.shared.infrastructure.persistence.sqlalchemy.unit_of_work import (
    DirtySQLAlchemySessionBeforeUnitOfWorkInitException,
    NoTransactionInitializedOnUnitOfWorkItemException,
)


class SqlAlchemyUnitOfWorkItem(UnitOfWorkItem):
    __UPPER_TRANSACTION_SESSION_KEY = "uow_upper_transaction"

    def __init__(self, db: SQLAlchemy) -> None:
        self.__db = db
        self.__transaction: Optional[SessionTransaction] = None

    def _start(self) -> None:
        session = self.__db.session()

        has_active_transaction = session.in_transaction() is True

        if has_active_transaction is False:
            self.__transaction = session.begin()
            self.__set_current_transaction_as_upper_in_session(session)
            return

        if session.info.get(self.__UPPER_TRANSACTION_SESSION_KEY) is None:
            self.__guard_current_session_is_not_dirty(session)
            self.__transaction = session.transaction
            self.__set_current_transaction_as_upper_in_session(session)
            return

        self.__transaction = session.begin_nested()

    def __set_current_transaction_as_upper_in_session(self, session: SignallingSession) -> None:
        session.info[self.__UPPER_TRANSACTION_SESSION_KEY] = self.__transaction

    def __guard_current_session_is_not_dirty(self, session: SignallingSession) -> None:
        is_upper_level_transaction = session.transaction.parent is None
        session_has_been_modified = self.__session_has_been_modified(session)
        if is_upper_level_transaction is True and session_has_been_modified is True:
            raise DirtySQLAlchemySessionBeforeUnitOfWorkInitException()

    def __session_has_been_modified(self, session: SignallingSession) -> bool:
        return bool(session.new or session.dirty or session.deleted)

    def _complete(self) -> None:
        self.__current_transaction().commit()
        self.__clear_transaction()

    def __current_transaction(self) -> SessionTransaction:
        if self.__transaction is None:
            raise NoTransactionInitializedOnUnitOfWorkItemException()

        return self.__transaction

    def __clear_transaction(self) -> None:
        if self.__current_transaction() is self.__db.session().info[self.__UPPER_TRANSACTION_SESSION_KEY]:
            del self.__db.session().info[self.__UPPER_TRANSACTION_SESSION_KEY]
        self.__transaction = None

    def _discard(self) -> None:
        self.__current_transaction().rollback()
        self.__clear_transaction()
