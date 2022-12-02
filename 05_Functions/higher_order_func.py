"""
Higher Order Functions:
=======================
Please note that this is an advanced topic, so it may take a couple of attempls
to understand these concepts.

Functions under the ood are just "Objects", they can be passed to other
functions and functions can also return functions!

This idata type is called "Callable", one which can be called or invoked.

Note:
=====
Till now we have been sending data to our functions, but sending data every time 
can be expensive, instead we can send functions to data!

Don't spend too much time mastering this topic, ti will com naturally as you 
progress with your programming skills.
"""
from typing import Callable


def hello() -> None:
    """Prints Hello World"""
    print("Hello World")


print(hello)
print(id(hello))
print(type(hello))

# we can assign function to variables

# just assigns the object 'hello to greet varaible
greet: Callable[[], None] = hello
greet()  # we can invoke/call the function using '()' at the end

# ================================================================================
"""
Let's try to create a universal greeter that can greet a person in multiple ways
"""


def zola(name: str) -> str:
    return f"Zola, {name}!"


def good_morning(name: str) -> str:
    return f"Good Morning, {name}!"


def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

# Function accepting funcion


def universal_greeter(name: str, greeter: Callable[[str], str]):
    """Can greet in multiple ways"""
    msg = greeter(name)
    print(msg)


universal_greeter('miclem', zola)
universal_greeter('miclem', good_morning)
universal_greeter('miclem', goodbye)

"""
Function returning functions!!
==============================

This can be confusing, relax if you can't get it, it took me serveral attaempts
to understan this!
"""

# Function returning a function


def add_by_5(num: int) -> Callable[[], int]:
    """Add by 5"""

    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(5)
print(sum())


# Function returning a function
def unique_adder(num1: int) -> Callable[[int], int]:
    """Adds two numbers and subtract by 1"""

    def adder(num2: int) -> int:
        return num1 + num2 - 1

    return adder


adder = unique_adder(5)
print(adder(6))
# adder = unique_adder(5)(5)  # ulternative syntax
# print(adder)


def testing_adder() -> Callable[[int], int]:
    """Adds 10 to a given number"""

    def add(num: int) -> int:
        return num + 10

    return add


testadd = testing_adder()
print(f"Testing adder is: {testadd(5)}")


# ================================================================================

"""
Lambda:
=======

Perhaps the most neglected, but very powerful technique to work with functions.
Again, don't spend too much time mastering it, it will com naturally!

The way in which we declared function are verbose, we can condense them in a 
single statement

Let's tye to create a calculate fro scratch
"""
add: Callable[[int, int], int] = lambda x, y: x + y
sub: Callable[[int, int], int] = lambda x, y: x - y
mul: Callable[[int, int], int] = lambda x, y: x * y

def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    """Perfoms some calculations based on the operation."""
    return operation(num1, num2)


print(calc(2, 4, add))
print(calc(5, 3, sub))
print(calc(3, 5, mul))
