import time
def memoize(func):
    def wrapper(*args, **kwargs):
        if(dict.get(args) != None):
            return dict[args[0]]
        else:
            return func(args[0])
    return wrapper

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

def timer(func):
    def wrappper(*args, **kwargs):
        start = time.time()
        func(args)
        end = time.time()
        return end - start
    return wrappper
        
@timer
@validate_args
@memoize 
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(20)
fibonacci(23)
a = fibonacci(24)
dict = {}
print(f"без мемоизации: {fibonacci(24)}, с мемоизацией: {a}")