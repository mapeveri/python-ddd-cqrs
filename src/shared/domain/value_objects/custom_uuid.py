import uuid


class Uuid:
    id: str

    def __init__(self, id: str):
        self.id = id

    def __str__(self) -> str:
        return self.id

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    def next() -> str:
        return str(uuid.uuid4().hex)
