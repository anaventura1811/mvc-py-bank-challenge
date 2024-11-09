from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.transaction import Payment
from src.models.sqlite.interfaces.transaction_interface import TransactionInterface


class PaymentTransactionRepository(TransactionInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_transaction(self, transaction: Payment) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(transaction)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def list_transactions(self, account_id: int) -> List[Payment]:
        with self.__db_connection as database:
            try:
                transactions = (
                    database.session
                    .query(Payment)
                    .filter(Payment.account_id == account_id)
                    .all()
                )
                return transactions
            except NoResultFound:
                return []

    def list_payment_transactions(self, account_id: int) -> List[Payment]:
        with self.__db_connection as database:
            try:
                transactions = (
                    database.session
                    .query(Payment)
                    .filter(Payment.account_id == account_id)
                    .all()
                )
                return transactions
            except NoResultFound:
                return []

    def get_transaction_by_id(self, transaction_id: int) -> Payment:
        with self.__db_connection as database:
            try:
                transaction = (
                    database.session
                    .query(Payment)
                    .filter(Payment.id == transaction_id)
                    .one()
                )
                return transaction
            except NoResultFound:
                return None
