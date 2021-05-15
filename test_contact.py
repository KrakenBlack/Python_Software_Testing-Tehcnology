from contact import Contact
import pytest

@pytest.fixture()
def valid_name():
    return 'Connect'
class TestCreateContact:

    def test_create_contact(self):

        contact = Contact()

        assert isinstance(contact,Contact)