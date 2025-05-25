def callLimit(limit: int):
    """blocks the execution of the function above a limit
    -> takes limit: max no. of allowed calls
    -> initilises count = 0
    -> returns decorator function callLimiter"""

    count = 0

    def callLimiter(function):
        """receives the function (eg. f() or g())
        and returns a wrapped version of the function limit_function"""

        def limit_function(*args: any, **kwds: any):
            """wrapper function that runs in place of the original function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
