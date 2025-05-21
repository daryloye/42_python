import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    S = sys.argv[1]
    N = sys.argv[2]

    # check arguments using list comprehension
    if not all(c.isalnum() for word in S.split() for c in word):
        raise AssertionError("the arguments are bad")
    if not N.isdigit():
        raise AssertionError("the arguments are bad")

    # check length of word using ft_filter & lambda
    checkLength = lambda word: len(word) > int(N)   # noqa:E731
    newList = list(ft_filter(checkLength, (word for word in S.split())))
    print(newList)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
