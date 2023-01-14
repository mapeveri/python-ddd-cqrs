import abc
from typing import Protocol, Optional

from src.marketplace.event.domain.file import File
from src.marketplace.event.domain.value_objects.file_id import FileId


class FileRepository(Protocol):
    @abc.abstractmethod
    def find_by_id(self, file_id: FileId) -> Optional[File]:
        ...

    @abc.abstractmethod
    def save(self, file: File) -> None:
        ...
