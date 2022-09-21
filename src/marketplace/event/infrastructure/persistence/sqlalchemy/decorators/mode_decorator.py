from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.mode import Mode


class ModeDecorator(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, mode: Mode, dialect) -> str:
        if mode is not None:
            return mode.value()

    def process_result_value(self, value: str, dialect) -> Mode:
        if value is not None:
            return Mode(value)
