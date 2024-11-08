from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_repository import LegalEntityRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(LegalEntityTable)
                 .filter(LegalEntityTable.customer_id == 123)
                 .first()],
                [LegalEntityTable(
                    customer_id=123,
                    cnpj="42.975.175/0001-64",
                    corporate_name="IT Test Holdings",
                    trade_name="IT Test",
                    establishment_date=date(2021, 8, 3).isoformat()
                )]
            )]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_legal_entity():
    mock_connection = MockConnection()
    repo = LegalEntityRepository(mock_connection)
    customer_id = 123
    repo.get_legal_entity(customer_id)
    mock_connection.session.query.assert_called_once_with(LegalEntityTable)
    mock_connection.session.filter.assert_called_once_with(
        LegalEntityTable.customer_id == customer_id)
    mock_connection.session.one.assert_called_once()
