from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.customer import CustomerTable
from src.models.sqlite.interfaces.customer_interface import CustomerInterface


class CustomerRepository(CustomerInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_customer(self, full_name: str, email: str, phone: str, cpf: str) -> None:
        with self.__db_connection as database:
            try:
                customer = (
                    CustomerTable(
                        full_name=full_name,
                        email=email,
                        phone=phone,
                        cpf=cpf,
                    )
                )
                database.session.add(customer)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_customer(self, email: str) -> CustomerTable:
        with self.__db_connection as database:
            try:
                customer = (
                    database.session
                    .query(CustomerTable)
                    .filter(CustomerTable.email == email)
                    .first()
                )
                return customer
            except NoResultFound:
                return None

    def update_customer(self, email: str, phone: str) -> CustomerTable:
        with self.__db_connection as database:
            try:
                updated_customer = (
                    database.session
                    .query(CustomerTable)
                    .filter(CustomerTable.email == email)
                    .update({CustomerTable.phone: phone}, sincronyze_session=True)
                    .one()
                )
                database.session.commit()
                return updated_customer
            except NoResultFound:
                database.session.rollback()
                return None
