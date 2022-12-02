"""
Variable & Keywoord Arguments:
==============================

What happens if we don't know before hand how many arguments we are 
going to reveive? we can handle this situation by using variable &
keyword arguments syntax.
j
Info:
=====
We will first look at unpacking first.
"""

from typing import Any
# ======================== Unpacking ==============================

first, last = ("Miclem", "Abasie")

print(first, last)

first, *rest = ['this', 'is', 'for', 'testing', 'unpacking']
print(first, rest)


specs = {'types': 'dynamic', 'optional': 'static typing', 'found': 'everywhere'}
# how to unpack a dictionary into an existing dictionary
lang = {'name': 'Python', **specs}

lang = {**specs}

# print(lang)


# ======================== Variable Argument ==============================

def unknown_friends(*args: str) -> None:
    # The argument is going to be of the type of tuple containing strings
    for friend in args:
        print(friend)


# unknown_friends('Miclem', 'Abasie', "Jack", "Micheal", "Jane", "Vicky")

# ======================== Keyword Argument ==============================


def unknown_products(**kwargs: Any) -> None:
    # The kwargs is always in the form of a dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


unknown_products(name="pizza", price=3.40, topping="olives", extra=True)

# ======================== Bringing it all together ==============================


def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice('Sneakers', 'black', 'white', brand_name='sniky',
        cat='Air jordan', in_stock=False)
