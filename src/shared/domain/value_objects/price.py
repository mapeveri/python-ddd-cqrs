from src.shared.domain.exceptions.price_exception import PriceException


class Price:
    amount: float

    def __init__(self, amount: float) -> None:
        self.__check_price(amount)
        self.amount = amount

    @staticmethod
    def __check_price(amount: float) -> None:
        if amount < 0:
            raise PriceException()

    def value(self) -> float:
        return self.amount
