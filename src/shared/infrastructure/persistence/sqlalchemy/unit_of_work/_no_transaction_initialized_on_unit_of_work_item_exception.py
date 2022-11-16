class NoTransactionInitializedOnUnitOfWorkItemException(Exception):
    def __init__(self) -> None:
        super().__init__("No transaction initialized on unit of work item")
