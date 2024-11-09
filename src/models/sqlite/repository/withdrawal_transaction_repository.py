from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface
from src.models.sqlite.entities.transaction import Withdrawal


class WithdrawalTransactionRepository(TransactionInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_transaction(self, transaction: Withdrawal) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(transaction)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def list_transactions(self, account_id: int) -> List[Withdrawal]:
        with self.__db_connection as database:
            try:
                transactions = (
                    database.session
                    .query(Withdrawal)
                    .filter(Withdrawal.account_id == account_id)
                    .all()
                )
                return transactions
            except NoResultFound:
                return []

    def get_transaction_by_id(self, transaction_id: int) -> Withdrawal:
        with self.__db_connection as database:
            try:
                transaction = (
                    database.session
                    .query(Withdrawal)
                    .filter(Withdrawal.id == transaction_id)
                    .one()
                )
                return transaction
            except NoResultFound:
                return None
