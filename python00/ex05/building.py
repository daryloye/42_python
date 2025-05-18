import sys


def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == ""):
        print("What is the text to count?")
        text = sys.stdin.read()
        # carriage return counts as a space, ctrl-D to end input
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        text = sys.argv[1]

    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for c in text if c.isupper())} upper letters")
    print(f"{sum(1 for c in text if c.islower())} lower letters")
    print(f"{sum(1 for c in text if c in punctuations)} punctuation marks")
    print(f"{sum(1 for c in text if c.isspace())} spaces")
    print(f"{sum(1 for c in text if c.isdigit())} digits")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
