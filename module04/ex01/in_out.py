def square(x: int | float) -> int | float:
    """returns the square of the argument"""
    return (x**2)


def pow(x: int | float) -> int | float:
    """returns the exponentiation of argument by itself"""
    return (x**x)


def outer(x: int | float, function) -> object:
    """returns an object that when called returns the
result of the arguments calculation"""
    count = 0
    value = x

    def inner() -> float:
        """applies the function to the stored value and updates it"""
        nonlocal count, value
        count += 1
        value = function(value)
        return value
    return inner
