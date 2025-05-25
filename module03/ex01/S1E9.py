from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract base class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Set first_name and is_alive status"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """Stark Class"""

    def __init__(self, first_name, is_alive=True):
        """Initialise Stark Character"""
        super().__init__(first_name, is_alive)
