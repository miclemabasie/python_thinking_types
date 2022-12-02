"""
Class:
======

'Class' are just like a building blueprint, they provide you with the
specification of how to construct a building. it is upto you when and
how you build the building.

Instance:
=========
When you actually construct a building out of the blueprint, it is called as
an 'Instance' or 'Object' of the class. So, both are related but essential
different terminology.

Class = Blueprint, Instance = Building

Methods:
========
These are just normal functions, but defined to alter the behavior of your instance
Since they are tied to a class, they are called as methods, Their behavior is depending
on the structure you define in the class.

When to use Class:
==================
use classes only when you need 'Structure' and 'Behavior' together.

If you only need structure, then choose from any existing data structure such as list,
tuple, dictionary, quiue, etc. Just need a behavior? Then just create a function that
transfrom your data.

"""

# =======================================================================================


class SomeClass:
    """Defines an empty class"""

    pass


print(SomeClass)

# =======================================================================================


class Person:
    """Defines a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def my_info(self):
        print(f"name: {self.name} and age: {self.age}")

    def __repr__(self) -> str:
        """Official Representation of the class"""
        return '<class "Person">'

    def __str__(self):
        """String Representation of an instance"""
        return f"Person -> name: {self.name}, age: {self.age}"

    def greet(self) -> None:
        """Method that performs a greet operation."""
        print(f"{self.name}, says hello!")


p1 = Person('miclem', 42)
p1.my_info()
p1.greet()
print(p1)
p2 = Person('cece', 4)
# print(p2)

# Both are different instances of the same class at different memory location
print(f"person1 is loacted at memory address: {hex(id(p1))}")
print(f"Person2 is located at memory address: {hex(id(p2))}")
