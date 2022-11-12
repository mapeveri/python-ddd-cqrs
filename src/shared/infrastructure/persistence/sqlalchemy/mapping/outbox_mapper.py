from datetime import datetime
from typing import Type

from sqlalchemy import Table, Column, String, Text, DateTime

from src.shared.domain.outbox.outbox import Outbox
from src.shared.infrastructure.persistence.sqlalchemy.decorators.outbox_id_decorator import (
    OutboxIdDecorator,
)
from src.shared.infrastructure.persistence.sqlalchemy.utils.mapper import Mapper


class OutboxMapper(Mapper):
    def _create_table(self) -> Table:
        return self._db_instance.Table(
            "outbox",
            Column("id", OutboxIdDecorator, primary_key=True),
            Column("aggregate_type", String(50), nullable=False),
            Column("aggregate_id", String(255), nullable=False),
            Column("type", String(255), nullable=False),
            Column("payload", Text, nullable=False),
            Column("created_at", DateTime, nullable=False, default=datetime.utcnow),
        )

    def entity(self) -> Type:
        return Outbox
