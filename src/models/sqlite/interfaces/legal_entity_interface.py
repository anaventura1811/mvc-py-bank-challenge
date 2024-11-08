from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_entity import LegalEntityTable


class LegalEntityInterface(ABC):

    @abstractmethod
    def insert_legal_entity(self, legal_entity: LegalEntityTable) -> None:
        pass

    @abstractmethod
    def get_legal_entity(self, customer_id: int) -> LegalEntityTable:
        pass
