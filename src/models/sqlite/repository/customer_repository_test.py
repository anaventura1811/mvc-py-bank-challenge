# from datetime import date
from src.models.sqlite.settings.connection import database_connection_handler
from .customer_repository import CustomerRepository


def test_get_customer():
    connection = database_connection_handler
    connection.connect_to_db()
    repo = CustomerRepository(connection)
    email = "anaventura1811@gmail.com"
    res = repo.get_customer(email)
    print(res)
