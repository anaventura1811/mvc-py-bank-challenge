import pytest
from sqlalchemy.engine import Engine
from .connection import database_connection_handler


@pytest.mark.skip(reason="teste")
def test_connection_to_database():
    assert database_connection_handler.get_engine() is None
    database_connection_handler.connect_to_db()
    db_engine = database_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
