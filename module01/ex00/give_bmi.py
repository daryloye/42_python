def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """take 2 lists of integers or floats in input,
    returns a list of BMI values"""

    if len(height) != len(weight):
        print("Lists are not the same length")
        return []

    if not all(isinstance(x, (int, float)) for x in height + weight):
        print("Lists must contain only int or float")
        return []

    return ([kg / (m * m) for kg, m in zip(weight, height)])


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """accepts a list of integers or floats
    and an integer representing a limit,
    returns a list of booleans (True if above the limit)"""

    if not all(isinstance(x, (int, float)) for x in bmi):
        print("List must contain only int or float")
        return []

    return ([b > limit for b in bmi])
