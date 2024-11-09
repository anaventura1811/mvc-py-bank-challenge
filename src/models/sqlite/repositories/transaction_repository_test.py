from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.transaction import TransactionTable
from .transaction_repository import TransactionRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(TransactionTable)
                 .filter(TransactionTable.id == 1234)
                 .one()],
                [TransactionTable(
                    id=1234,
                    account_id=123,
                    value=2000.00,
                    date=date(2024, 10, 1).isoformat(),
                    transaction_limit=3000.00,
                    balance_after_transaction=1000.00,
                )]
            ), (
                [mock.call.query(TransactionTable)
                 .filter(TransactionTable.account_id == 123)
                 .all()],
                [TransactionTable(
                    id=1234,
                    account_id=123,
                    value=2000.00,
                    date=date(2024, 10, 1).isoformat(),
                    transaction_limit=3000.00,
                    balance_after_transaction=1000.00,
                )]
            )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_transaction_by_id():
    mock_connection = MockConnection()
    repo = TransactionRepository(mock_connection)
    transaction_id = 1234
    repo.get_transaction_by_id(transaction_id)
    mock_connection.session.query.assert_called_once_with(TransactionTable)
    mock_connection.session.filter.assert_called_once_with(
        TransactionTable.id == transaction_id)
    mock_connection.session.one.assert_called_once()

def test_list_transactions():
    mock_connection = MockConnection()
    repo = TransactionRepository(mock_connection)
    account_id = 123
    repo.list_transactions(account_id=account_id)
    mock_connection.session.query.assert_called_once_with(TransactionTable)
    mock_connection.session.filter.assert_called_once_with(
        TransactionTable.account_id == account_id)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.one.assert_not_called()
