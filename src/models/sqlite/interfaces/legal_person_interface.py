from abc import ABC, abstractmethod
from datetime import date
from src.models.sqlite.entities.legal_person import LegalPersonTable


class LegalPersonInterface(ABC):

    @abstractmethod
    def insert_legal_person(self,
                            customer_id: int,
                            cpf: str,
                            birth_date: date) -> None:
        pass

    @abstractmethod
    def get_legal_person(self, customer_id: int) -> LegalPersonTable:
        pass
