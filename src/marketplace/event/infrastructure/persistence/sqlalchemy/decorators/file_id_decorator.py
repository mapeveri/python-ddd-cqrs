from typing import Any, Optional

from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.file_id import FileId


class FileIdDecorator(TypeDecorator):
    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, file_id: Any, dialect: Any) -> Optional[str]:
        if isinstance(file_id, str):
            return str(file_id)

        if file_id is not None:
            return str(file_id)

        return None

    def process_result_value(self, value: Any, dialect: Any) -> Optional[FileId]:
        if value is not None:
            return FileId(value)

        return None
