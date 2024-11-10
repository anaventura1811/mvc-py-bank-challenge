from typing import Dict
from datetime import datetime
from src.models.sqlite.entities.transaction import Deposit
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from src.models.sqlite.interfaces.account_interface import AccountInterface
from .interfaces.transaction_creator_controller import TransactionCreatorControllerInterface


class DepositCreatorController(TransactionCreatorControllerInterface):
    def __init__(self,
                 transaction_repository: TransactionInterface,
                 account_repository: AccountInterface) -> None:
        self.__transaction_repository = transaction_repository
        self.__account_repository = account_repository

    def create(self, transaction: Dict) -> Dict:
        self.__validate_transaction(transaction)
        current_balance = self.__get_current_balance_in_db(transaction["account_id"])
        transaction_limit = self.__generate_transaction_limit(current_balance)
        formatted_transaction = self.__generate_transaction_from_dict(
            transaction, current_balance, transaction_limit)
        self.__insert_transaction_in_db(formatted_transaction)
        response = self.__format_response(formatted_transaction)
        return response

    def __validate_transaction(self, transaction: Dict) -> None:
        if "account_id" not in transaction:
            raise Exception("Payload inválido!")
        if "value" not in transaction:
            raise Exception("Payload inválido!")
        if not isinstance(transaction["value"], float):
            raise Exception("Payload inválido!")
        if transaction["value"] <= 0.0:
            raise Exception("Payload inválido!")

    def __get_current_balance_in_db(self, account_id: int) -> float:
        account = self.__account_repository.get_account_by_id(account_id)
        if account:
            return account.balance
        raise Exception('Conta não encontrada')

    def __generate_transaction_limit(self, balance: float) -> float:
        now = datetime.now().hour
        if now > 20 or now <= 6:
            return 1000.00
        return balance

    def __generate_transaction_from_dict(
            self, payload: Dict, current_balance: float, transaction_limit: float) -> Deposit:
        updated_value = current_balance + payload["value"]
        transaction = {
            "account_id": payload["account_id"],
            "value": payload["value"],
            "date": datetime.now().isoformat(),
            "balance_after_transaction": updated_value if updated_value > 0 else 0.0,
            "description": payload.get("description", "Pagamento"),
            "transaction_limit": transaction_limit,
        }
        return Deposit(
            account_id=transaction["account_id"],
            value=transaction["value"],
            date=transaction["date"],
            balance_after_transaction=transaction["balance_after_transaction"],
            transaction_limit=transaction["transaction_limit"],
            description=transaction["description"]
        )

    def __insert_transaction_in_db(self, transaction: Deposit) -> None:
        self.__transaction_repository.create_transaction(transaction)
        self.__account_repository.update_account_balance(
            transaction.account_id,
            transaction.balance_after_transaction)

    def __format_response(self, transaction: Deposit) -> Dict:

        return {
            "data": {
                "type": "Deposit",
                "count": 1,
                "attributes": {
                    "id": transaction.id,
                    "account_id": transaction.account_id,
                    "value": transaction.value,
                    "date": transaction.date,
                    "description": transaction.description,
                    "balance_after_transaction": transaction.balance_after_transaction,
                    "transaction_limit": transaction.transaction_limit
                },
            }
        }
