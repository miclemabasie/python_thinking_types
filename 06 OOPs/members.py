"""
Class can have class variables as well as intance variables.

Class variables are shared across all instance while instance 
variables are only limited to that particular instance.
"""


class Box:

    # class Variables
    box_type = "Packagin Carton"
    color = "Brown"

    def __init__(self, side_a: int, side_b: int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self) -> str:
        return f"<class 'Box'>"

    def __str__(self) -> str:
        return f"Side A is: {self.side_a} and Side B is: {self.side_b}"


b1 = Box(3, 5)
print(b1)
print(b1.box_type)
print(b1.color)
