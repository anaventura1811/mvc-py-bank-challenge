from datetime import date
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.transaction import Payment
from .payment_transaction_repository import PaymentTransactionRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(Payment)
                 .filter(Payment.id == 1234)
                 .one()],
                [Payment(
                    id=1234,
                    account_id=123,
                    value=2000.00,
                    date=date(2024, 10, 1).isoformat(),
                    transaction_limit=3000.00,
                    balance_after_transaction=1000.00,
                )]
            ), (
                [mock.call.query(Payment)
                 .filter(Payment.account_id == 123)
                 .all()],
                [Payment(
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
    repo = PaymentTransactionRepository(mock_connection)
    transaction_id = 1234
    repo.get_transaction_by_id(transaction_id)
    mock_connection.session.query.assert_called_once_with(Payment)
    mock_connection.session.filter.assert_called_once_with(
        Payment.id == transaction_id)
    mock_connection.session.one.assert_called_once()

def test_list_transactions():
    mock_connection = MockConnection()
    repo = PaymentTransactionRepository(mock_connection)
    account_id = 123
    repo.list_transactions(account_id=account_id)
    mock_connection.session.query.assert_called_once_with(Payment)
    mock_connection.session.filter.assert_called_once_with(
        Payment.account_id == account_id)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.one.assert_not_called()
