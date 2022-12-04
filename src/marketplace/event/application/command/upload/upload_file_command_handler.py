import os
from dataclasses import dataclass
from typing import Optional

from src.marketplace.event.application.command.upload.upload_file_command import UploadFileCommand
from src.shared.domain.bus.command.command_handler import CommandHandler


@dataclass
class UploadFileCommandHandler(CommandHandler):
    def __init__(self, upload_folder: str) -> None:
        self.__upload_folder = upload_folder

    def __call__(self, command: UploadFileCommand) -> None:
        content = command.content
        path = command.path
        filename = os.path.join(self.__upload_folder, path)

        if command.chunk:
            chunk_range = command.chunk_range
            self.__save_chunk_file(content, filename, chunk_range)
            return

        self.__save_complete_file(content, filename)

    def __save_complete_file(
        self,
        content: bytes,
        filename: str,
    ) -> None:
        with open(filename, "ab+") as f:
            f.write(content)

    def __save_chunk_file(self, content: bytes, filename: str, chunk_range: Optional[int]) -> None:
        with open(filename, "ab+") as f:
            f.seek(chunk_range)
            f.write(content)
