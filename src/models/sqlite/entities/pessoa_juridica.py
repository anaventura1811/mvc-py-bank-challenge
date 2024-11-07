from sqlalchemy import Column, BIGINT, REAL, TEXT, INTEGER
from src.models.sqlite.settings.base import Base


class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    idade = Column(INTEGER, nullable=False)
    nome_fantasia = Column(TEXT, nullable=False)
    email_corporativo = Column(TEXT, nullable=False, unique=True)
    categoria = Column(TEXT, nullable=False)
    celular = Column(TEXT, nullable=False, unique=True)
    faturamento = Column(REAL, nullable=True)
    saldo = Column(REAL, nullable=False)
