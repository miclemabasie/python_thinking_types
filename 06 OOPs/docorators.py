"""
Decorators:
===========
They are used to implement particular behavior for out classes.

Summary:
========
1. Property - Acts like a instane variable, no need to call like function.
2. Static method - Directly called from the class.
3. Class method - Returns a new instance of the class.
4. getters & setters - Used for 'Data Encapsulation'.

Info:
=====
We can mark the class as 'final' so that no other class can subclass it.

"""


class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property
    def fullname(self) -> str:
        """
        The @property decorator allows us to call the function 
        as tho it was an instance variable (person.fullname)
        """
        return f"{self.fname} {self.lname}"


p1 = Person("Miclem", "Abasie")
print(p1)
print(p1.fullname)
