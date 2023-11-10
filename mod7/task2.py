dict = {}

def memoize(func):
    def wrapper(*args, **kwargs):
        if(dict.get(args) != None):
            return dict[args[0]]
        else:
            return func(args[0])
    return wrapper

@memoize          
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

