from sqlalchemy import Column, BIGINT, TEXT, DATE, ForeignKey
from src.models.sqlite.settings.base import Base


class LegalEntityTable(Base):
    __tablename__ = "legal_entity"

    id = Column(BIGINT, primary_key=True)
    cnpj = Column(TEXT, nullable=False, unique=True)
    trade_name = Column(TEXT, nullable=False)
    corporate_name = Column(TEXT, nullable=False)
    establishment_date = Column(DATE, nullable=False)
    customer_id = Column(BIGINT, ForeignKey('customer.id'))

    def __repr__(self):
        company_data = f"cnpj={self.cnpj}, trade_name={self.trade_name}"
        cpn_data = f"corporate_name={self.corporate_name}"
        date = f"establishment_date={self.establishment_date}"

        return f"LegalEntity [{company_data}, {cpn_data}, {date}]"
