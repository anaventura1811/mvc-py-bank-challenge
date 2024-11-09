from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.transaction import TransactionTable


class TransactionInterface(ABC):

    @abstractmethod
    def create_transaction(self, transaction: TransactionTable) -> None:
        pass

    @abstractmethod
    def list_transactions(self, account_id: int) -> List[TransactionTable]:
        pass

    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> TransactionTable:
        pass
