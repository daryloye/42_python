import sys
from ft_filter import ft_filter

def main():
    if len(sys.argv) != 3:
        raise AssertionError("the argumnets are bad")
    
    print(filter.__doc__)
    print(ft_filter.__doc__)

    ft_filter()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
