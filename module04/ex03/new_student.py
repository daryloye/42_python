import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """returns a list of k items randomly chosen from string.ascii_lowercase"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """sets fields where init=False"""
        self.active = True
        self.login = self.name[0] + self.surname
        self.id = generate_id()
