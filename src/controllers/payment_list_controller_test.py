from datetime import date
from src.models.sqlite.entities.transaction import Payment
from .payment_list_controller import PaymentListController


class MockPaymentRepository:
    def list_transactions(self, account_id: int):
        return [
            Payment(
                date=date(2024, 11, 9).isoformat(),
                id=123,
                account_id=account_id,
                balance_after_transaction=1600,
                value=200,
                description="Transferência para Fulano de Tal"),
            Payment(
                date=date(2024, 11, 8).isoformat(),
                id=122,
                account_id=account_id,
                balance_after_transaction=1800,
                value=200,
                description="Transferência para Fulano de Tal")]


def test_list_transactions():
    controller = PaymentListController(MockPaymentRepository())
    account_id = 456
    response = controller.list(account_id)

    formatted_transactions = [{"date": "2024-11-09", "type": "payment",
                               "id": 123, "account_id": 456, "balance_after_transaction": 1600,
                               "value": 200, "description": "Transferência para Fulano de Tal"},
                              {"date": "2024-11-08", "type": "payment", "id": 122,
                               "account_id": 456,
                               "balance_after_transaction": 1800,
                               "value": 200, "description": "Transferência para Fulano de Tal"}]
    expected_response = {
        "data": {
            "type": "Payment",
            "count": 2,
            "attributes": formatted_transactions
        }
    }

    assert "data" in response
    assert response == expected_response
