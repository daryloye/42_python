class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of 2 vectors"""
        res = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of of 2 vectors"""
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction of of 2 vectors"""
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
