from abc import ABC, abstractmethod
from typing import Dict
from src.models.sqlite.entities.customer import CustomerTable


class CustomerInterface(ABC):

    @abstractmethod
    def insert_customer(self, customer_data: Dict) -> CustomerTable:
        pass

    @abstractmethod
    def get_customer(self, email: str) -> CustomerTable:
        pass
