from dataclasses import dataclass
from typing import List

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_repository import OutboxRepository


@dataclass
class SqlAlchemyOutboxRepository(OutboxRepository):
    db: SQLAlchemy = Provide['db']

    def save(self, outbox: Outbox) -> None:
        self.db.session.add(outbox)
        self.db.session.flush()
        self.db.session.commit()

    def find_all_by_order_by_created_at_asc(self) -> List[Outbox]:
        return self.db.session.query(Outbox).all().order_by(Outbox.created_at.asc())
