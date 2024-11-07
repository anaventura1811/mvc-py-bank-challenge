from typing import Dict
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.customer import CustomerTable
from src.models.sqlite.interfaces.customer_interface import CustomerInterface


class CustomerRepository(CustomerInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_customer(self, customer_data: Dict) -> None:
        with self.__db_connection as database:
            try:
                customer = (
                    CustomerTable(
                        full_name=customer_data["full_name"],
                        email=customer_data["email"],
                        birth_date=customer_data["birth_date"],
                        customer_type=customer_data["customer_type"],
                        phone=customer_data["phone"]
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
