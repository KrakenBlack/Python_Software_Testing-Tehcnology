
class Contact:


    def __init__(self, name,home_phone = None, mob_phone = None, email = ''):

        if home_phone is None and mob_phone is None:
            raise ValueError

        if not home_phone.startswith("+372"):
            raise ValueError

        if '@' in email:
            self.email = email
        else:
            self.email = ''