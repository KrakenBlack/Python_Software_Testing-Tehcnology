from contact import Contact
import pytest

@pytest.fixture()
def valid_name():
    return 'Connect'\

@pytest.fixture()
def valid_phone():
    return ''

@pytest.fixture()
def valid_mob():
    return ''


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
        name = ''


        with pytest.raises(ValueError):
            contact = Contact(name)

    @pytest.mark.skip(reason = 'Not implemented')
    def test_with_invalid_countrycode(self):
        pass

    @pytest.mark.skip(reason='Not implemented')
    def test_with_invalid_email(self):
        pass