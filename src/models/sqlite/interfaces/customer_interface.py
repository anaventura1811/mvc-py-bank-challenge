from abc import ABC, abstractmethod
from src.models.sqlite.entities.customer import CustomerTable


class CustomerInterface(ABC):

    @abstractmethod
    def insert_customer(self, full_name: str, email: str, phone: str, cpf: str) -> None:
        pass

    @abstractmethod
    def get_customer(self, email: str) -> CustomerTable:
        pass

    @abstractmethod
    def update_customer(self, email: str, phone: str) -> CustomerTable:
        pass
