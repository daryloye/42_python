def count_in_list(lst: list, find: str) -> int:
    """Counts how many times a given element appears in a list"""

    return sum(1 for elem in lst if elem == find)
