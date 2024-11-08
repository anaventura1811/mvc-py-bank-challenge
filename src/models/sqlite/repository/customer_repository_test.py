from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.customer import CustomerTable
from .customer_repository import CustomerRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[(
                [mock.call.query(CustomerTable)
                 .filter(CustomerTable.email == "ana@teste.com")
                 .first()],
                [CustomerTable(full_name="Ana Ventura",
                               email="ana@teste.com",
                               phone="83 99999-9999",
                               cpf="00000000000")]
            )]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_get_customer():
    mock_connection = MockConnection()
    repo = CustomerRepository(mock_connection)
    email = "ana@teste.com"
    repo.get_customer(email)
    mock_connection.session.query.assert_called_once_with(CustomerTable)
    mock_connection.session.filter.assert_called_once_with(CustomerTable.email == email)
    mock_connection.session.first.assert_called_once()
