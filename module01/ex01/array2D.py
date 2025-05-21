def slice_me(family: list, start: int, end: int) -> list:
    """takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array
    based on the provided start and end arguments."""

    if not all(isinstance(lst, list) for lst in family):
        print("not a list")
        return []

    if not all(len(lst) == len(family[0]) for lst in family):
        print("lists are not the same size")
        return []

    print(f"My shape is : ({len(family)}, {len(family[0])})")

    sli = slice(start, end)
    newFamily = family[sli]
    print(f"My new shape is : ({len(newFamily)}, {len(newFamily[0])})")

    return newFamily
