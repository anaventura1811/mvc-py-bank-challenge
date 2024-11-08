from abc import ABC, abstractmethod
from typing import Dict


class CustomerProfileInterface(ABC):

    @abstractmethod
    def insert_customer_profile(self, customer_data: Dict) -> None:
        pass
