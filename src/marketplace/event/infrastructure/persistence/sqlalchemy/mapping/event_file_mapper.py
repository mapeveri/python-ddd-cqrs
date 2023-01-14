from typing import Type

from sqlalchemy import Table, Column, String

from src.marketplace.event.domain.file import File
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.event_id_decorator import (
    EventIdDecorator,
)
from src.marketplace.event.infrastructure.persistence.sqlalchemy.decorators.file_id_decorator import FileIdDecorator
from src.shared.infrastructure.persistence.sqlalchemy.utils.mapper import Mapper


class EventFileMapper(Mapper):
    def _create_table(self) -> Table:
        return self._db_instance.Table(
            "event_file",
            Column("id", FileIdDecorator, primary_key=True),
            Column("file", String(200), nullable=False),
            Column("event_id", EventIdDecorator, nullable=False),
        )

    def entity(self) -> Type:
        return File
