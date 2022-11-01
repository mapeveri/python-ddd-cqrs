from src.shared.domain.exceptions import PriceException


class Price:
    amount: float

    def __init__(self, amount: float):
        self.__validate_price(amount)
        self.amount = amount

    @staticmethod
    def __validate_price(amount: float):
        if amount < 0:
            raise PriceException('Invalid price')

    def value(self) -> float:
        return self.amount
