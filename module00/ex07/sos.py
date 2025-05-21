import sys

NESTED_MORSE = {
    " ": "/ ",
    'A': '.- ',    'B': '-... ',  'C': '-.-. ',  'D': '-.. ',
    'E': '. ',     'F': '..-. ',  'G': '--. ',   'H': '.... ',
    'I': '.. ',    'J': '.--- ',  'K': '-.- ',   'L': '.-.. ',
    'M': '-- ',    'N': '-. ',    'O': '--- ',   'P': '.--. ',
    'Q': '--.- ',  'R': '.-. ',   'S': '... ',   'T': '- ',
    'U': '..- ',   'V': '...- ',  'W': '.-- ',   'X': '-..- ',
    'Y': '-.-- ',  'Z': '--.. ',

    '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
    '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
    '8': '---.. ', '9': '----. '
}


def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    try:
        out = ''.join(NESTED_MORSE[c.upper()] for c in sys.argv[1])
        print(out.strip())
    except Exception:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
