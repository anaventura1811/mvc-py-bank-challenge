from abc import ABC, abstractmethod
from typing import Dict


class TransactionListControllerInterface(ABC):

    @abstractmethod
    def list(self, account_id: int) -> Dict:
        pass
