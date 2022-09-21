from sqlalchemy.types import TypeDecorator, NUMERIC

from src.shared.domain.value_objects.price import Price


class PriceDecorator(TypeDecorator):
    impl = NUMERIC

    def process_bind_param(self, price: Price, dialect) -> float:
        if price is not None:
            return price.value()

    def process_result_value(self, value: float, dialect) -> Price:
        if value is not None:
            return Price(value)
