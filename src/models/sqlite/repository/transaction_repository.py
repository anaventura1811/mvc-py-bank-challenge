from typing import List, Dict
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.transaction import TransactionTable
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface


class TransactionRepository(TransactionInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_transaction(self, transaction: TransactionTable) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(transaction)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def generate_transaction_from_dict(self, payload: Dict) -> TransactionTable:
        transaction = TransactionTable(
            account_id=payload["account_id"],
            value=payload["value"],
            date=payload["date"],
            balance_after_transaction=payload["balance_after_transaction"],
            transaction_limit=payload["transaction_limit"]
        )
        return transaction

    def get_transaction_by_id(self, transaction_id: int) -> TransactionTable:
        with self.__db_connection as database:
            try:
                transaction = (
                    database.session
                    .query(TransactionTable)
                    .filter(TransactionTable.id == transaction_id)
                    .one()
                )
                return transaction
            except NoResultFound:
                return None

    def list_transactions(self, account_id: int) -> List[TransactionTable]:
        with self.__db_connection as database:
            try:
                transactions = (
                    database.session
                    .query(TransactionTable)
                    .filter(TransactionTable.account_id == account_id)
                    .all()
                )
                return transactions
            except NoResultFound:
                return []
