"""
Since Zortan has less gravity, residents can fly if they weigh
less than or equal to 15Kgs in zoratn weight

Louis wants to see which of his friends can fly.

Info:
=====
Our functions do only one thing at a time, This is called as
`Single Responsibility Principle` and important aspect of programming
"""
from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15


def convert_weight(weight: float) -> float:
    """
    Calculates Zoratn Weight
    ========================

    Look how the function just transforms data, from float to float
    """
    zortan_weight = (weight + 32) / 8
    return zortan_weight


def can_fly(weight: float) -> bool:
    """
    Returns if you can fly or not
    =============================

    This function is a nice example for data transformation,
    we convert float value to boolean value.
    """

    if weight <= MAX_FLYING_WEIGHT:
        return True
    else:
        return False


def flying_friends(friends: dict) -> None:
    """
    Displays flying and non-flying friends

    Note:
    =====
    No data transformation here.
    we are printing the ouput to console, the function doesn't return anything.
    """

    for friend, weight in friends.items():
        # Check if the friend's weight is less than 15 in zortan
        zortan_weight = convert_weight(weight)
        if can_fly(zortan_weight):
            print(f"{friend} weighs {zortan_weight} in Zortan, So he can fly!")
        else:
            print(f"{friend} weighs {weight} in zortan, so he can only walk.")


def main() -> None:
    friends: dict[str, float, ] = {
        "Cece": 54,
        'Roko': 88,
        'Chiko': 50,
        'Niko': 102,
        'Ziko': 90,
    }

    flying_friends(friends)


if __name__ == '__main__':
    main()
