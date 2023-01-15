from src.marketplace.event.domain.value_objects.file_id import FileId


class FileAlreadyExistsException(Exception):
    def __init__(self, file_id: FileId) -> None:
        self.file_id = file_id
        super().__init__(f"File with id {str(file_id)} already exists")
