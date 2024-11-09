from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict


class Client(ABC):

    @abstractmethod
    def generate_bank_statement(self,
                                init_date: datetime, end_date: datetime, client_id: int) -> Dict:
        pass

    @abstractmethod
    def make_a_withdrawal(self, amount: float, client_id: int) -> Dict:
        pass
