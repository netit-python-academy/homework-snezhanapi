from enum import Enum


class Role(Enum):
    User = "User"
    Admin = "Admin"


class StandardUser:
    def __str__(self) -> str:
        return f"{self._name}, {self._role.value}"

    def __init__(self, first_name: str, last_name: str, email: str, phone: str, password: str, role: Role):
        self._name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._role = role
        self._password = password

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password


class Administrator(StandardUser):
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, password: str):
        super().__init__(first_name, last_name, email, phone, password, Role.Admin)


class User(StandardUser):
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, password: str):
        super().__init__(first_name, last_name, email, phone, password, Role.User)