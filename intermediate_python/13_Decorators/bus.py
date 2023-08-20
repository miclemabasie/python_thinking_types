from lib import add
from functools import wraps


def add_decorator(func):
    @wraps(func)
    def wrapper(x, y):
        if y == 0 and x != 0:
            # Reverse the numbers
            a = x
            x = y
            y = a
            a = func(x, y)
        return a

    return wrapper


add = add_decorator(add)

print(add(2, 0))

print(help(add))
print(add.__name__)
