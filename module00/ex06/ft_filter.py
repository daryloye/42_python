def ft_filter(function, iterable) -> object:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))

# print(filter.__doc__)
# print(ft_filter.__doc__)

# ages = [5, 12, 17, 18, 24, 32, False, True]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# # myFunc
# adults = ft_filter(myFunc,ages)
# for x in adults:
# 	print(x)

# # None
# adults = ft_filter(None, ages)
# for x in adults:
# 	print(x)
