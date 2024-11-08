from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_person import LegalPersonTable
from .legal_person_repository import LegalPersonRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(LegalPersonTable)
                 .filter(LegalPersonTable.customer_id == 123)
                 .first()],
                [LegalPersonTable(
                    customer_id=123,
                    cpf="00000000000",
                    birth_date=date(1990, 11, 18).isoformat(),
                )]
            )]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_legal_person():
    mock_connection = MockConnection()
    repo = LegalPersonRepository(mock_connection)
    customer_id = 123
    repo.get_legal_person(customer_id)
    mock_connection.session.query.assert_called_once_with(LegalPersonTable)
    mock_connection.session.filter.assert_called_once_with(
        LegalPersonTable.customer_id == customer_id)
    mock_connection.session.first.assert_called_once()
