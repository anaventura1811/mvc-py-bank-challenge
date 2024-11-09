from datetime import date
import pytest
from src.models.sqlite.entities.transaction import Deposit
from .deposit_list_controller import DepositListController


class MockDepositRepository:
    def list_transactions(self, account_id: int):
        return [
            Deposit(
                date=date(2024, 11, 9).isoformat(),
                id=123,
                account_id=account_id,
                balance_after_transaction=2000,
                value=200,
                description="Transferência de Fulano de Tal"),
            Deposit(
                date=date(2024, 11, 8).isoformat(),
                id=122,
                account_id=account_id,
                balance_after_transaction=1800,
                value=200,
                description="Transferência de Fulano de Tal")]


def test_list_transactions():
    controller = DepositListController(MockDepositRepository())
    account_id = 456
    response = controller.list(account_id)

    formatted_transactions = [{"date": "2024-11-09", "type": "deposit",
                               "id": 123, "account_id": 456, "balance_after_transaction": 2000,
                               "value": 200, "description": "Transferência de Fulano de Tal"},
                              {"date": "2024-11-08", "type": "deposit", "id": 122,
                               "account_id": 456,
                               "balance_after_transaction": 1800,
                               "value": 200, "description": "Transferência de Fulano de Tal"}]
    expected_response = {
        "data": {
            "type": "Deposit",
            "count": 2,
            "attributes": formatted_transactions
        }
    }

    assert "data" in response
    assert response == expected_response


def test_list_transaction_error():
    controller = DepositListController(MockDepositRepository())
    account_id = "456"
    with pytest.raises(Exception) as exc:
        controller.list(account_id)
        assert str(exc) == 'Payload inválido!'
