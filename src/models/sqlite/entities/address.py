from sqlalchemy import Column, BIGINT, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class AddressTable(Base):
    __tablename__ = "address"

    id = Column(BIGINT, primary_key=True)
    customer_id = Column(BIGINT, ForeignKey('customer.id'))
    street = Column(TEXT, nullable=False)
    city = Column(TEXT, nullable=False)
    state = Column(TEXT, nullable=False)
    zip_code = Column(TEXT, nullable=False)
    customer = relationship("Customer", back_populates="address")

    def __repr__(self):
        address = f"street={self.street}, city={self.city}, state={self.state}"
        postal_code = f"postal_code={self.postal_code}"
        return f"CustomerProfile [address_id={self.id}, {address}, {postal_code}]"
