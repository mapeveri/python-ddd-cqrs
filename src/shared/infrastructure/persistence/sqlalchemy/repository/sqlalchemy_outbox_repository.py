from dataclasses import dataclass
from typing import List

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from src.shared.domain.outbox.outbox import Outbox
from src.shared.domain.outbox.outbox_criteria import OutboxCriteria
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

    def find_by_criteria(self, criteria: OutboxCriteria) -> List[Outbox]:
        return (
            self.db.session.query(Outbox)
            .order_by(text(criteria.order_by))
            .limit(criteria.limit)
            .with_for_update(skip_locked=True, of=Outbox)
        )
