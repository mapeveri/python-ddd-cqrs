class InvalidParameterException(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid value in parameters")
