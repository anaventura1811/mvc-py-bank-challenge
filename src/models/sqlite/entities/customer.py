from sqlalchemy import Column, BIGINT, TEXT, DATE, String
# from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class CustomerTable(Base):
    __tablename__ = "customer"

    id = Column(BIGINT, primary_key=True)
    email = Column(TEXT, nullable=False, unique=True)
    full_name = Column(TEXT, nullable=False)
    birth_date = Column(DATE, nullable=False)
    customer_type = Column(String, nullable=False)
    phone = Column(TEXT, nullable=False)
    # addresses = relationship("Address", back_populates="customer")
    # profiles = relationship("CustomerProfile", back_populates="customer")

    def __repr__(self):
        personal_data = f"full_name={self.full_name}, birth_date={self.birth_date}"
        customer_data = f"customer_type={self.customer_type}"
        personal_contact_data = f"email={self.email}, phone={self.phone}"

        return f"Customer [{personal_data}, {customer_data}, {personal_contact_data}]"
