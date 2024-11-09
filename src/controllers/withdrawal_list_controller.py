from typing import Dict, List
from src.models.sqlite.entities.transaction import Withdrawal
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from .interfaces.transaction_list_controller import TransactionListControllerInterface


class WithdrawalListController(TransactionListControllerInterface):
    def __init__(self, withdrawal_repository: TransactionInterface) -> None:
        self.__withdrawal_repository = withdrawal_repository

    def list(self, account_id: int) -> Dict:
        self.__validate_account_id(account_id)
        transactions = self.__list_transactions_in_db(account_id)
        response = self.__format_response(transactions)
        return response

    def __validate_account_id(self, account_id: int) -> None:
        if not account_id or isinstance(account_id, int) is not True:
            raise Exception('Payload inválido!')

    def __list_transactions_in_db(self, account_id: int) -> List[Withdrawal]:
        transactions = self.__withdrawal_repository.list_transactions(account_id)
        return transactions

    def __format_response(self, transactions: List[Withdrawal]) -> Dict:
        formatted_transactions = [{
            "date": transaction.date,
            "type": transaction.type,
            "id": transaction.id,
            "account_id": transaction.account_id,
            "balance_after_transaction": transaction.balance_after_transaction,
            "value": transaction.value,
            "description": transaction.description} for transaction in transactions]
        return {
            "data": {
                "type": "Withdrawal",
                "count": len(formatted_transactions),
                "attributes": formatted_transactions,
            }
        }
