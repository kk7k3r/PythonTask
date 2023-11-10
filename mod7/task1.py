def validate_args(func):
    def wrapper(*args, **kwargs):
        if (len(args) < 1):
            return "Not enough arguments"
        if (len(args) > 1):
            return "Too many arguments"
        if (not (isinstance(args[0], int))):
            return "Wrong types"
        if (int(args[0]) < 0):
            return "Negative argument"
        return func(args[0])
    return wrapper

@validate_args
def do(a):
    return a

print(do())
