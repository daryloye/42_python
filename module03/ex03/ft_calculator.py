class calculator:
    """Calculator class"""

    def __init__(self, object) -> None:
        """Initialise the Calculator"""
        self.object = object

    def __add__(self, object) -> None:
        """Add a number"""
        self.object = [o + object for o in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """Multiply a number"""
        self.object = [o * object for o in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """Subtract a number"""
        self.object = [o - object for o in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """Divide a number"""
        if object == 0:
            print("cannot divide by 0")
            return
        self.object = [o / object for o in self.object]
        print(self.object)
