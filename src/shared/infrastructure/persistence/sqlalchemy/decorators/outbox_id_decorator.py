from sqlalchemy.types import TypeDecorator, VARCHAR

from src.shared.domain.value_objects.outbox_id import OutboxId


class OutboxIdDecorator(TypeDecorator):
    impl = VARCHAR

    cache_ok = True

    def process_bind_param(self, outbox_id, dialect) -> str:
        if isinstance(outbox_id, str):
            return outbox_id

        if outbox_id is not None:
            return str(outbox_id)

    def process_result_value(self, value, dialect) -> OutboxId:
        if value is not None:
            return OutboxId(value)
