from sqlalchemy import Column, BIGINT, ForeignKey, TEXT
from src.models.sqlite.settings.base import Base


class AddressTable(Base):
    __tablename__ = "address"

    id = Column(BIGINT, primary_key=True)
    customer_id = Column(BIGINT, ForeignKey('customer.id'))
    street = Column(TEXT, nullable=False)
    street_number = Column(TEXT, nullable=True)
    complement = Column(TEXT, nullable=True)
    city = Column(TEXT, nullable=False)
    state = Column(TEXT, nullable=False)
    zip_code = Column(TEXT, nullable=False)

    def __repr__(self):
        address = f"street={self.street}, city={self.city}, state={self.state}"
        complement = f"street_number={self.street_number}, complement={self.complement}"
        zip_code = f"zip_code={self.zip_code}"

        return f"Address [{address}, {complement}, {zip_code}]"
