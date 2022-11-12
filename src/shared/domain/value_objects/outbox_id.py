from src.shared.domain.value_objects.custom_uuid import Uuid


class OutboxId(Uuid):
    def __init__(self, id: str) -> None:
        super(OutboxId, self).__init__(id)

    def __hash__(self) -> int:
        return hash(self.id)
