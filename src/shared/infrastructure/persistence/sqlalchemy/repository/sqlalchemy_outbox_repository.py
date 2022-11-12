from dataclasses import dataclass
from typing import List

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_repository import OutboxRepository
from src.shared.domain.value_objects.outbox_id import OutboxId


@dataclass
class SqlAlchemyOutboxRepository(OutboxRepository):
    db: SQLAlchemy = Provide["db"]

    def save(self, outbox: Outbox) -> None:
        self.db.session.add(outbox)
        self.db.session.flush()

    def remove(self, outbox_id: OutboxId) -> None:
        self.db.session.query(Outbox).filter(Outbox.id == outbox_id.id).delete()

    def find_by_order_by_created_at_asc(self) -> List[Outbox]:
        return self.db.session.query(Outbox).order_by(Outbox.created_at.asc()).limit(100).with_for_update()
