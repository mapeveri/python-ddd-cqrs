class DirtySQLAlchemySessionBeforeUnitOfWorkInitException(Exception):
    def __init__(self) -> None:
        super().__init__(
            "SQLAlchemy session has been used to create, update or delete items before unit of work was initialized"
        )
