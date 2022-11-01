from src.shared.domain.value_objects.custom_uuid import Uuid


class OutboxId(Uuid):
    def __init__(self, id: str):
        super(OutboxId, self).__init__(id)

    def __hash__(self):
        return hash(self.id)
