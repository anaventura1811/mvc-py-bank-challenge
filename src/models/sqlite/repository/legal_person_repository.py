from datetime import date
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.legal_person_interface import LegalPersonInterface
from src.models.sqlite.entities.legal_person import LegalPersonTable


class LegalPersonRepository(LegalPersonInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_legal_person(self, customer_id: int, cpf: str, birth_date: date) -> None:
        with self.__db_connection as database:
            try:
                legal_person = (
                    LegalPersonTable(
                        customer_id=customer_id,
                        cpf=cpf,
                        birth_date=birth_date
                    )
                )
                database.session.add(legal_person)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_legal_person(self, customer_id: int) -> LegalPersonTable:
        with self.__db_connection as database:
            try:
                legal_person = (
                    database.session
                    .query(LegalPersonTable)
                    .filter(LegalPersonTable.customer_id == customer_id)
                    .first()
                )
                return legal_person
            except NoResultFound:
                return None
