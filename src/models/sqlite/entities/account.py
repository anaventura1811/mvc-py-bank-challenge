from sqlalchemy import Column, BIGINT, ForeignKey, REAL
from sqlalchemy.orm import relationship
from src.models.sqlite.settings.base import Base


class AccountTable(Base):
    __tablename__ = "account"

    id = Column(BIGINT, primary_key=True)
    customer_profile_id = Column(BIGINT, ForeignKey('customer_profile.id'))
    balance = Column(REAL, default=0.0)
    revenue = Column(REAL, default=0.0)
    customer_profile = relationship("CustomerProfile", back_populates="account")
    transactions = relationship("Transaction", back_populates="account")

    def __repr__(self):
        return f"CustomerProfile [account_id={self.id}, balance={self.balance}]"
