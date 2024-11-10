from datetime import datetime
import pytest
from src.models.sqlite.entities.account import AccountTable
from src.models.sqlite.entities.transaction import Payment
from .payment_creator_controller import PaymentCreatorController


class MockAccountRepository:
    def get_account_by_id(self, account_id: int) -> AccountTable:
        return AccountTable(
            id=account_id,
            account_number=12345,
            customer_id=1,
            balance=1000.00,
            revenue=0.0,
            created_at=datetime.now().isoformat(),
            legal_entity_id=1)

    def update_account_balance(self, account_id: int, new_balance: float) -> None:
        pass


class MockPaymentRepository:
    def create_transaction(self, transaction: Payment) -> None:
        pass


def test_create_payment():
    transaction = {
        "account_id": 1,
        "value": 180.00,
        "description": "Transferência para Fulana"
    }

    controller = PaymentCreatorController(
        payment_repository=MockPaymentRepository(), account_repository=MockAccountRepository())
    response = controller.create(transaction)
    assert "data" in response
    assert "type" in response["data"]
    assert "count" in response["data"]
    assert "attributes" in response["data"]
    assert response["data"]["type"] == "Payment"
    assert response["data"]["count"] == 1
    assert "value" in response["data"]["attributes"]


def test_create_payment_error():
    transaction = {
        "value": "180.00",
        "description": "Transferência para Fulana"
    }
    controller = PaymentCreatorController(
        payment_repository=MockPaymentRepository(), account_repository=MockAccountRepository())

    with pytest.raises(Exception) as exc:
        controller.create(transaction)
        assert str(exc.value) is not None
        assert str(exc.value) == "Payload inválido!"
