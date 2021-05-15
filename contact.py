
class Contact:


    def __init__(self, name,home_phone = None, mob_phone = None):
        self.name = name

        if home_phone is None and mob_phone is None:
            raise ValueError

