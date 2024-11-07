from sqlalchemy import Column, BIGINT, REAL, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class TransactionTable(Base):
    __tablename__ = 'transaction'

    id = Column(BIGINT, primary_key=True)
    account_id = Column(BIGINT, ForeignKey('account.id'))
    type = Column(String, nullable=False)
    amount = Column(REAL, nullable=False)
    date = Column(DATETIME, nullable=False)
    account = relationship("Account", back_populates="transaction")

    def __repr__(self):
        transaction_data = f"type={self.type}, amount={self.amount}"

        return f"Transaction [id={self.id}, {transaction_data}, date={self.date}]"
