from sqlalchemy import Column, BIGINT, REAL, String, ForeignKey, DATETIME
from src.models.sqlite.settings.base import Base


class TransactionTable(Base):
    __tablename__ = 'transaction'

    id = Column(BIGINT, primary_key=True)
    account_id = Column(BIGINT, ForeignKey('account.id'))
    type = Column(String, nullable=False)
    value = Column(REAL, nullable=False)
    date = Column(DATETIME, nullable=False)
    balance_after_transaction = Column(REAL, nullable=False, default=0.0)
    transaction_limit = Column(REAL, nullable=False, default=0.0)

    def __repr__(self):
        transaction_data = f"type={self.type}, value={self.value}, date={self.date}"
        balance = f"balance_after_transaction={self.balance_after_transaction}"
        limit = f"transaction_limit={self.transaction_limit}"

        return f"Transaction [{transaction_data}, {balance}, {limit}]"
