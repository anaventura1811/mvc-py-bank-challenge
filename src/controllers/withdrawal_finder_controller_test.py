from datetime import date
import pytest
from src.models.sqlite.entities.transaction import Withdrawal
from .withdrawal_finder_controller import WithdrawalFinderController


class MockWithdrawalRepository:
    def get_transaction_by_id(self, transaction_id: int):
        return Withdrawal(date=date(2024, 11, 9).isoformat(),
                          id=transaction_id,
                          account_id=456,
                          balance_after_transaction=1600,
                          value=200,
                          transaction_limit=1600,
                          description="Transferência de Fulano de Tal")


def test_find_transaction():
    controller = WithdrawalFinderController(MockWithdrawalRepository())
    transaction_id = 123
    response = controller.find(transaction_id)

    expected_response = {
        "data": {
            "type": "Withdrawal",
            "count": 1,
            "attributes": {"id": 123,
                           "account_id": 456,
                           "description": "Transferência de Fulano de Tal",
                           "value": 200,
                           "date": "2024-11-09",
                           "balance_after_transaction": 1600,
                           "transaction_limit": 1600}
        }
    }

    assert "data" in response
    assert response == expected_response


def test_find_transaction_error():
    controller = WithdrawalFinderController(MockWithdrawalRepository())
    transaction_id = 456
    with pytest.raises(Exception) as exc:
        controller.find(transaction_id)
        assert str(exc) == 'Transação não encontrada!'
