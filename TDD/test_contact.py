from contact import Contact
import pytest


@pytest.fixture()
def valid_name():
    return 'Connect'\

@pytest.fixture()
def valid_phone():
    return '+0 56569999'

@pytest.fixture()
def valid_mob():
    return '+0 5656 1111'

@pytest.fixture()
def invalid_email():
    return 'sda.com'

class TestCreateContact:
    # def test_create_contact_with_args(self,valid_name,valid_phone,valid_mob):
    #     # imput
    #     name = valid_name
    #     phone = valid_phone
    #     mob = valid_mob
    #
    #
    #     # process
    #     contact = Contact(name, phone, mob)
    #
    #     #asserting
    #     assert isinstance(contact,Contact)
    #     assert contact.name == name
    #     assert contact.phone == phone
    #     assert contact.mob == mob

    def test_without_any_number(self):


        with pytest.raises(ValueError):
            contact = Contact(valid_name)

    # @pytest.mark.skip(reason = 'Not implemented')
    def test_with_invalid_country_code(self,valid_name, valid_phone):

        with pytest.raises(ValueError):
            contact = Contact(valid_name, home_phone=valid_phone)

    # @pytest.mark.skip(reason='Not implemented')
    def test_with_invalid_email(self,valid_name,invalid_email):
        contact = Contact(valid_name, home_phone= '+372 5656 999',email = invalid_email)

        assert contact.email == ''