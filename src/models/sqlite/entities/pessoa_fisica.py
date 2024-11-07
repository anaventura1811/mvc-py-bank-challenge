from sqlalchemy import Column, BIGINT, REAL, TEXT
from src.models.sqlite.settings.base import Base


class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True)
    nome_completo = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False, unique=True)
    celular = Column(TEXT, nullable=False, unique=True)
    idade = Column(BIGINT, nullable=False)
    categoria = Column(TEXT, nullable=False)
    saldo = Column(REAL, nullable=False)
    renda_mensal = Column(REAL, nullable=True)
