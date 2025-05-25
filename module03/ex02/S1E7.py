from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class"""

    def __init__(self, first_name, is_alive=True):
        """Initialise Baratheon Character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """called by print(obj) or str(obj)"""
        return f"{self.first_name} {self.family_name} says hello"

    def __repr__(self):
        """called by repr(obj)"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Lannister Class"""

    def __init__(self, first_name, is_alive=True):
        """Initialise Lannister Character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """called by print(obj) or str(obj)"""
        return f"{self.first_name} {self.family_name} says hello"

    def __repr__(self):
        """called by repr(obj)"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create Lannister Character in a chain"""
        return cls(first_name, is_alive)
