from typing import Any, Optional

from sqlalchemy.types import TypeDecorator, VARCHAR

from src.marketplace.event.domain.value_objects.mode import Mode


class ModeDecorator(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, mode: Mode, dialect: Any) -> Optional[str]:
        if mode is not None:
            return mode.value()

        return None

    def process_result_value(self, value: str, dialect: Any) -> Optional[Mode]:
        if value is not None:
            return Mode(value)

        return None
