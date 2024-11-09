from abc import ABC, abstractmethod
from typing import Optional
from src.models.sqlite.entities.account import AccountTable


class AccountInterface(ABC):

    @abstractmethod
    def create_account(self,
                       customer_id: int,
                       acc_type: str,
                       balance: float,
                       revenue: Optional[float] = None) -> None:
        pass

    @abstractmethod
    def get_account_by_customer_id(self, customer_id: int) -> AccountTable:
        pass

    @abstractmethod
    def update_account_balance(self, account_id: int, new_balance: float) -> None:
        pass
