from sqlalchemy import Column, BIGINT, TEXT, DATETIME
from src.models.sqlite.settings.base import Base


class CustomerTable(Base):
    __tablename__ = "customer"

    id = Column(BIGINT, primary_key=True)
    full_name = Column(TEXT, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    email = Column(TEXT, nullable=False, unique=True)
    phone = Column(TEXT, nullable=False)
    cpf = Column(TEXT, nullable=False, unique=True)

    def __repr__(self):
        personal_data = f"full_name={self.full_name}, cpf={self.cpf}"
        customer_data = f"created_at={self.created_at}"
        personal_contact_data = f"email={self.email}, phone={self.phone}"

        return f"Customer [{personal_data}, {customer_data}, {personal_contact_data}]"
