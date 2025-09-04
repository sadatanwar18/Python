'''
What is decorator:

A decorator is a function that modifoes the behaviour of another function or class without
changing its actual code
it is applied using the @decorator_name syntax

Think of it like wrapping a gift — you don’t change the gift, but you add extra features (wrapper, bow, etc.).

In python functions are forst class citizen:
-> functions can be stored in variables
-> passed as arguments
-> returned from other functions
'''

# Basic Decorator

# a decorator takes a function as input, wraps it with extra loguc, and return it

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("after function call")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()


# decorator with arguments

# we use *args and **kwargs to hanldle any arguments

def my_new_decorator(func):
    def wrapper(*args, **kwargs):
        print("before function call")
        res = func(*args, **kwargs)
        print("after function call")
        return res
    return wrapper

@my_new_decorator
def add (a,b):
    return a + b

print(add(5,3))


# preserving meta data (functools.wraps)

# decorator overwrite metadata (__name__, __doc__)
#solution: use functools.wraps

from functools import wraps

def this_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Now, add.__name__ will still be "add" instead of "wrapper".


def log_activity(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        print (f"calling : {func.__name__}")
        result = func(*args , **kwargs)
        print (f"Finished : {func.__name__}")
        return result
    return wrapper

@log_activity
def logger(user):
    print(f"{user} loggin in!")

logger("Sadat")



def auth(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
        else:
            return func(user_role)
    
    return wrapper

@auth
def inventory_access(role):
    print("Access granted to inventory")

inventory_access("admin")
inventory_access("user")