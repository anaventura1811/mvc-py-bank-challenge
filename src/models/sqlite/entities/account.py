from sqlalchemy import Column, BIGINT, ForeignKey, REAL, TEXT, DATETIME
from src.models.sqlite.settings.base import Base


class AccountTable(Base):
    __tablename__ = "account"

    id = Column(BIGINT, primary_key=True)
    customer_id = Column(BIGINT, ForeignKey('customer.id'))
    balance = Column(REAL, default=0.0)
    revenue = Column(REAL, default=0.0)
    type = Column(TEXT, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    legal_person_id = Column(BIGINT, ForeignKey('legal_person.id'), nullable=True)
    legal_entity_id = Column(BIGINT, ForeignKey('legal_entity.id'), nullable=True)

    def __repr__(self):
        legal_status1 = f"legal_person_id={self.legal_person_id}"
        legal_status2 = f"legal_entity_id={self.legal_entity_id}"
        acc_data = f"balance={self.balance}, revenue={self.revenue}"
        date = f"created_at={self.created_at}"

        return f"Account [{acc_data}, {date}, {legal_status1}, {legal_status2}]"
