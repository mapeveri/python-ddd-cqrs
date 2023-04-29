import os
from typing import Optional

from src.marketplace.event.application.command.upload.upload_event_file_command import UploadEventFileCommand
from src.marketplace.event.domain.exceptions.file_already_exists_exception import FileAlreadyExistsException
from src.marketplace.event.domain.file import File
from src.marketplace.event.domain.file_repository import FileRepository
from src.marketplace.event.domain.value_objects.event_id import EventId
from src.marketplace.event.domain.value_objects.file_id import FileId
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.domain.unit_of_work import UnitOfWork


class UploadEventFileCommandHandler(CommandHandler):
    def __init__(self, upload_folder: str, unit_of_work: UnitOfWork, file_repository: FileRepository) -> None:
        self.__upload_folder = upload_folder
        self.__unit_of_work = unit_of_work
        self.__file_repository = file_repository

    def __call__(self, command: UploadEventFileCommand) -> None:
        file_id = FileId(command.id)
        self.__check_file_does_not_exists(file_id)

        path = command.path
        content = command.content
        filename = os.path.join(self.__upload_folder, path)

        if command.chunk:
            chunk_range = command.chunk_range
            self.__upload_chunk_file(content, filename, chunk_range)
            return

        self.__upload_complete_file(content, filename)
        self.__save_file(file_id, filename, command.event_id)

    def __check_file_does_not_exists(self, file_id: FileId) -> None:
        file = self.__file_repository.find_by_id(file_id)
        if file is not None:
            raise FileAlreadyExistsException(file_id)

    def __upload_chunk_file(self, content: bytes, filename: str, chunk_range: Optional[int]) -> None:
        with open(filename, "ab+") as f:
            f.seek(chunk_range)
            f.write(content)

    def __upload_complete_file(self, content: bytes, filename: str) -> None:
        with open(filename, "ab+") as f:
            f.write(content)

    def __save_file(self, file_id: FileId, filename: str, event_id: str) -> None:
        with self.__unit_of_work():
            file = File.create(file_id, filename, EventId(event_id))
            self.__file_repository.save(file)
