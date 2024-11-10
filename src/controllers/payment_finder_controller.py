from typing import Dict
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from src.models.sqlite.entities.transaction import Payment
from .interfaces.transaction_finder_controller import TransactionFinderControllerInterface


class PaymentFinderController(TransactionFinderControllerInterface):

    def __init__(self, payment_repository: TransactionInterface) -> None:
        self.__payment_repository = payment_repository

    def find(self, transaction_id: int) -> Payment:
        payment = self.__find_payment_on_db(transaction_id)
        response = self.__format_response(payment)
        return response

    def __find_payment_on_db(self, transaction_id: int) -> Payment:
        payment = self.__payment_repository.get_transaction_by_id(transaction_id)
        if not payment:
            raise Exception('Transação não encontrada')
        return payment

    def __format_response(self, transaction: Payment) -> Dict:
        return {
            "data": {
                "type": "Payment",
                "count": 1,
                "attributes": {
                    "id": transaction.id,
                    "account_id": transaction.account_id,
                    "description": transaction.description,
                    "value": transaction.value,
                    "date": transaction.date,
                    "balance_after_transaction": transaction.balance_after_transaction,
                    "transaction_limit": transaction.transaction_limit,
                }
            }
        }
