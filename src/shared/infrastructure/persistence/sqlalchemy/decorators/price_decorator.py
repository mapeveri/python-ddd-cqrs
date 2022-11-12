from typing import Any, Optional

from sqlalchemy.types import TypeDecorator, NUMERIC

from src.shared.domain.value_objects.price import Price


class PriceDecorator(TypeDecorator):
    impl = NUMERIC

    def process_bind_param(self, price: Price, dialect: Any) -> Optional[float]:
        if price is not None:
            return price.value()

        return None

    def process_result_value(self, value: float, dialect: Any) -> Optional[Price]:
        if value is not None:
            return Price(value)

        return None
