def mean(args):
    """prints the mean"""
    ret = sum(args) / len(args)
    print(f"mean : {ret}")


def median(args):
    """prints the median"""
    ret = args[int(len(args) / 2)]
    print(f"median : {ret}")


def quartile(args):
    """prints the quartiles"""
    q1 = args[int(len(args) / 4)]
    q2 = args[int(len(args) / 4 * 3)]
    ret = [float(q1), float(q2)]
    print(f"quartile : {ret}")


def std_dev(args):
    mean = sum(args) / len(args)
    var = sum((x - mean)**2 for x in args) / len(args)
    ret = var**0.5
    print(f"std : {ret}")


def variance(args):
    """prints the variance"""
    mean = sum(args) / len(args)
    ret = sum((x - mean)**2 for x in args) / len(args)
    print(f"var : {ret}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """print statistics of *args according to **kwargs"""
    args = sorted(args)

    for value in kwargs.values():
        if len(args) == 0:
            print("ERROR")
            continue
        match value:
            case "mean":
                mean(args)
            case "median":
                median(args)
            case "quartile":
                quartile(args)
            case "std":
                std_dev(args)
            case "var":
                variance(args)
