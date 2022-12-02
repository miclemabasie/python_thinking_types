from enum import Enum, auto


class PizaaSize (Enum):
    """Pizza Base Size Options"""

    SMALL = 8
    MEDUIM = 10
    LARGE = 12


choice = PizaaSize.MEDUIM

print(f"One Order for {choice.value} inch pizza.")


class Color(Enum):
    """T-Shirt Varieties"""

    RED = 'RED'
    BLUE = 'BLUE'
    GREEN = 'GREEN'


print(f"One order for {Color.GREEN.value} T-Shirt")


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


print(Role.MANAGER.value)
