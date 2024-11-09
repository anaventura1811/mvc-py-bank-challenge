from datetime import date
from src.models.sqlite.entities.transaction import TransactionTable
from .transaction_list_controller import TransactionListController


class MockTransactionRepository:
    def list_transactions(self, account_id: int):
        return [
            TransactionTable(
                date=date(2024, 11, 9).isoformat(),
                id=123,
                account_id=account_id,
                balance_after_transaction=1600,
                value=200,
                description="Pagamento agendado"),
            TransactionTable(
                date=date(2024, 11, 8).isoformat(),
                id=122,
                account_id=account_id,
                balance_after_transaction=1800,
                value=200,
                description="Pagamento agendado")]


def test_list_transactions():
    controller = TransactionListController(MockTransactionRepository())
    account_id = 456
    response = controller.list(account_id)

    formatted_transactions = [{"date": "2024-11-09", "type": "transaction",
                               "id": 123, "account_id": 456, "balance_after_transaction": 1600,
                               "value": 200, "description": "Pagamento agendado"},
                              {"date": "2024-11-08", "type": "transaction", "id": 122,
                               "account_id": 456,
                               "balance_after_transaction": 1800,
                               "value": 200, "description": "Pagamento agendado"}]
    expected_response = {
        "data": {
            "type": "Transaction",
            "count": 2,
            "attributes": formatted_transactions
        }
    }

    assert "data" in response
    assert response == expected_response
