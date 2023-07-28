import random
import string


class Password:
    """Password"""

    def __init__(self, name):
        self.__name = str(name)
        self.__username = str
        self.__password = str
        self.__url = str
        self.__category = "No category"

    @property
    def name(self):
        """Getter name"""
        return self.__name

    @property
    def username(self):
        """Getter username"""
        return self.__username

    @property
    def password(self):
        """Getter password"""
        return self.__password

    @property
    def url(self):
        """Getter url"""
        return self.__url

    @property
    def category(self):
        """Getter category"""
        return self.__category

    @name.setter
    def name(self, value):
        self.__name = value

    @username.setter
    def username(self, value):
        self.__username = value

    @password.setter
    def password(self, value):
        self.__password = value

    @url.setter
    def url(self, value):
        self.__url = value

    @category.setter
    def category(self, value):
        self.__category = value

    def gen_pwd(self, length_pwd, min_numbers, min_special):
        """Generate password"""
        length_pwd -= min_numbers + min_special
        self.__password = (
            random.choices(string.ascii_letters, k=length_pwd)
            + random.choices(string.digits, k=min_numbers)
            + random.choices("!@#$%^&*", k=min_special)
        )
        random.shuffle(self.__password)
        self.__password = "".join(self.__password)
        return self.__password
