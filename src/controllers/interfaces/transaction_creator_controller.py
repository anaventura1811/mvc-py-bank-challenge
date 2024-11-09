from abc import ABC, abstractmethod
from typing import Dict


class TransactionCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, transaction: Dict) -> Dict:
        pass
