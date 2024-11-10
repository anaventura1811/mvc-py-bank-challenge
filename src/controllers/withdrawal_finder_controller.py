from typing import Dict
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from src.models.sqlite.entities.transaction import Withdrawal
from .interfaces.transaction_finder_controller import TransactionFinderControllerInterface


class WithdrawalFinderController(TransactionFinderControllerInterface):

    def __init__(self, withdrawal_repository: TransactionInterface) -> None:
        self.__withdrawal_repository = withdrawal_repository

    def find(self, transaction_id: int) -> Withdrawal:
        withdrawal = self.__find_withdrawal_on_db(transaction_id)
        response = self.__format_response(withdrawal)
        return response

    def __find_withdrawal_on_db(self, transaction_id: int) -> Withdrawal:
        withdrawal = self.__withdrawal_repository.get_transaction_by_id(transaction_id)
        if not withdrawal:
            raise Exception('Transação não encontrada')
        return withdrawal

    def __format_response(self, transaction: Withdrawal) -> Dict:
        return {
            "data": {
                "type": "Withdrawal",
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
