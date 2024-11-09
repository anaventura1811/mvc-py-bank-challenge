from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.account import AccountTable
from .account_le_repository import AccountLegalEntityRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(AccountTable)
                 .filter(AccountTable.customer_id == 123)
                 .first()],
                [AccountTable(
                    customer_id=123,
                    balance=2000.80,
                    created_at=date(2024, 10, 1).isoformat(),
                    legal_entity_id=1,
                )]
            )]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_account_by_customer_id():
    mock_connection = MockConnection()
    repo = AccountLegalEntityRepository(mock_connection)
    customer_id = 123
    repo.get_account_by_customer_id(customer_id)
    mock_connection.session.query.assert_called_once_with(AccountTable)
    mock_connection.session.filter.assert_called_once_with(
        AccountTable.customer_id == customer_id)
    mock_connection.session.one.assert_called_once()
