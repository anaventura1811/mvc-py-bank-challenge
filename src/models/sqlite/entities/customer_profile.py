from sqlalchemy import Column, BIGINT, TEXT, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class CustomerProfileTable(Base):
    __tablename__ = "customer_profile"

    id = Column(BIGINT, primary_key=True)
    customer_id = Column(BIGINT, ForeignKey('customer.id'))
    acc_type = Column(String, nullable=False)
    cpf = Column(TEXT, nullable=True, unique=True)
    cnpj = Column(TEXT, nullable=True, unique=True)
    customer = relationship("Customer", back_populates="customer_profile")
    accounts = relationship("Account", back_populates="customer_profile")

    def __repr__(self):
        customer_data = f"customer_id={self.customer_id}, cpf={self.cpf}, cnpj={self.cnpj}"

        return f"CustomerProfile [acc_type={self.type}, {customer_data}]"
