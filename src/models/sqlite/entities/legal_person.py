from sqlalchemy import Column, BIGINT, TEXT, DATE, ForeignKey
# from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class LegalPersonTable(Base):
    __tablename__ = "legal_person"

    id = Column(BIGINT, primary_key=True)
    cpf = Column(TEXT, ForeignKey('customer.cpf'))
    customer_id = Column(BIGINT, ForeignKey('customer.id'))
    birth_date = Column(DATE, nullable=False)

    def __repr__(self):
        return f"LegalPerson [cpf={self.cpf}, birth_date={self.birth_date}]"
