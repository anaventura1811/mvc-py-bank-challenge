from typing import Dict
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from src.models.sqlite.entities.transaction import Deposit
from .interfaces.transaction_finder_controller import TransactionFinderControllerInterface


class DepositFinderController(TransactionFinderControllerInterface):

    def __init__(self, deposit_repository: TransactionInterface) -> None:
        self.__deposit_repository = deposit_repository

    def find(self, transaction_id: int) -> Dict:
        deposit = self.__find_deposit_on_db(transaction_id)
        response = self.__format_response(deposit)
        return response

    def __find_deposit_on_db(self, transaction_id: int) -> Deposit:
        deposit = self.__deposit_repository.get_transaction_by_id(transaction_id)
        if not deposit:
            raise Exception('Transação não encontrada')
        return deposit

    def __format_response(self, transaction: Deposit) -> Dict:
        return {
            "data": {
                "type": "Deposit",
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
