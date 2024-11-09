from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.account_interface import AccountInterface
from src.models.sqlite.entities.account import AccountTable
from src.models.sqlite.entities.legal_entity import LegalEntityTable


class AccountLegalEntityRepository(AccountInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_account(self,
                       customer_id: int,
                       acc_type: str,
                       balance: float,
                       revenue: float | None = None) -> None:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.customer_id == customer_id)
                    .one()
                )
                account = (
                    AccountTable(
                        customer_id=customer_id,
                        balance=balance,
                        acc_type=acc_type,
                        revenue=revenue,
                        created_at=datetime.now(),
                        legal_entity_id=legal_entity.id)
                )
                database.session.add(account)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_account_by_customer_id(self, customer_id: int) -> AccountTable:
        with self.__db_connection as database:
            try:
                account = (
                    database.session
                    .query(AccountTable)
                    .filter(AccountTable.customer_id == customer_id)
                    .one()
                )
                return account
            except NoResultFound:
                return None

    def get_current_balance(self, account_id: int) -> float:
        with self.__db_connection as database:
            try:
                balance = (
                    database.session
                    .query(AccountTable)
                    .filter(AccountTable.id == account_id)
                    .one()
                )
                return balance.balance
            except NoResultFound:
                return 0.0

    def update_account_balance(self, account_id: int, new_balance: float) -> None:
        with self.__db_connection as database:
            try:
                updated_account = (
                    database.session
                    .query(AccountTable)
                    .filter(AccountTable.id == account_id)
                    .update({AccountTable.balance: new_balance}, sincronyze_session=True)
                    .one()
                )
                database.session.commit()
                return updated_account
            except NoResultFound:
                database.session.rollback()
                return None
