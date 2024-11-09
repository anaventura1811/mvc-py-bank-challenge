from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.legal_entity_interface import LegalEntityInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable


class LegalEntityRepository(LegalEntityInterface):

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity(self, legal_entity: LegalEntityTable) -> None:

        with self.__db_connection as database:
            try:
                database.session.add(legal_entity)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_legal_entity(self, customer_id: int) -> LegalEntityTable:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(
                        LegalEntityTable.customer_id == customer_id)
                    .one()
                )
                return legal_entity
            except NoResultFound:
                return None
