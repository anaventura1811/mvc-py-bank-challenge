from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.transaction import Withdrawal
from .withdrawal_transaction_repository import WithdrawalTransactionRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(Withdrawal)
                 .filter(Withdrawal.id == 1234)
                 .one()],
                [Withdrawal(
                    id=1234,
                    account_id=123,
                    value=2000.00,
                    date=date(2024, 10, 1).isoformat(),
                    transaction_limit=3000.00,
                    balance_after_transaction=1000.00,
                )]
            ), (
                [mock.call.query(Withdrawal)
                 .filter(Withdrawal.account_id == 123)
                 .all()],
                [Withdrawal(
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
    repo = WithdrawalTransactionRepository(mock_connection)
    transaction_id = 1234
    repo.get_transaction_by_id(transaction_id)
    mock_connection.session.query.assert_called_once_with(Withdrawal)
    mock_connection.session.filter.assert_called_once_with(
        Withdrawal.id == transaction_id)
    mock_connection.session.one.assert_called_once()

def test_list_transactions():
    mock_connection = MockConnection()
    repo = WithdrawalTransactionRepository(mock_connection)
    account_id = 123
    repo.list_transactions(account_id=account_id)
    mock_connection.session.query.assert_called_once_with(Withdrawal)
    mock_connection.session.filter.assert_called_once_with(
        Withdrawal.account_id == account_id)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.one.assert_not_called()
