from abc import ABC, abstractmethod
from src.models.sqlite.entities.transaction import TransactionTable


class TransactionFinderControllerInterface(ABC):

    @abstractmethod
    def find(self, transaction_id: int) -> TransactionTable:
        pass
