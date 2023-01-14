from dataclasses import dataclass
from typing import Optional

from dependency_injector.wiring import Provide
from flask_sqlalchemy import SQLAlchemy

from src.marketplace.event.domain.file import File
from src.marketplace.event.domain.file_repository import FileRepository
from src.marketplace.event.domain.value_objects.file_id import FileId


@dataclass
class SqlAlchemyFileRepository(FileRepository):
    db: SQLAlchemy = Provide["db"]

    def find_by_id(self, file_id: FileId) -> Optional[File]:
        return self.db.session.query(File).filter_by(id=file_id).one_or_none()

    def save(self, file: File) -> None:
        self.db.session.add(file)
        self.db.session.flush()
