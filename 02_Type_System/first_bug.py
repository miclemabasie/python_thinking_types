"""
First Bug
---------

Undesired behavior in programming is called a 'Bug'.

Python is a dynamically typed languate so it's easy to introduce a bug.
"""

box = "ballons"

print(f"box contains {box}")

box = 10
print(f"box contains {box}")


# ---------------------------------------------------------------------------------
# Introducing 'Type Hinting' - Optional Static Type Checking in Python using 'Mypy'
# ---------------------------------------------------------------------------------

food: str = 'Milk'
print(f"Louis is going to dring {food}")

food = "Eggs"
print(f"Louis is going to eat: {food}")

food = False
print(f"Louis is going to eat: {food}")
