import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()


class DatabaseConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = os.getenv('CONNECTION_STRING')
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        self.session.query().update()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


database_connection_handler = DatabaseConnectionHandler()
