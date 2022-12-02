"""
Let's convert the game login into small functions.

PRINCIPLES:
===========

1. DRY -> Don't Repeat Yourself.
================================
Try to keep your code as DRY as possible, group common functionality into
individual functions.

2. SRP -> Single Responsibility Principle.
==========================================
Ideally one function should be responsible for only one operation.

Note:
=====
We will also learn about global & local scope of variables (Using scratch pad)
"""

# importing the stuff we require
from random import randint
from typing import Final, Any


# ===============================================================================
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int ] is so boring, so we instead
# Create a type of alias and make our lives simpler.
# ===============================================================================

character = dict[str, str | int]


def get_superheroes() -> list[character]:
    # Super Heroes
    IRONMAN: Final[character] = {
        'name': 'Ironman', 'attack_power': 250, 'life': 100}
    BLACKWIDOW: Final[character] = {
        'name': 'BlackWidow', 'attack_power': 1000, 'life': 800}
    SPIDERMAN: Final[character] = {
        'name': 'SpiderMan', 'attack_power': 190, 'life': 700}
    HULK: Final[character] = {
        'name': 'Hulk', 'attack_power': 500, 'life': 1500}

    superheros: list[character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheros


def get_villains() -> list[character]:
    # Super Villains
    THANOS: Final[character] = {
        'name': 'Thanos', 'attack_power': 1500, 'life': 1500}
    REDSKULL: Final[character] = {
        'name': 'RedSkull', 'attack_power': 300, 'life': 800}
    PROXIMA: Final[character] = {
        'name': 'Proxima', 'attack_power': 320, 'life': 800}

    villains: list[character] = [THANOS, REDSKULL, PROXIMA]
    return villains


def get_superhero(index: int) -> character | None:
    """Retrun a super hero from a given index"""
    superheros = get_superheroes()
    if index < len(superheros):
        return superheros[index]
    else:
        return None


def get_villain(index: int) -> character | None:
    """Return a Villain from a given index"""
    villains = get_villains()
    if index < len(villains):
        villain = villains[index]
        return villain
    else:
        return None


def get_random_indexes(fight_team: str) -> int:
    """
    Takes in the current fight team and return a random index based on the 
    lenght of the team.
    """
    # get the lenght of the superheroes list
    superheroes_len = len(get_superheroes())
    villains_len = len(get_villains())
    # Get a random integer for indexing the both fighters
    if fight_team == 'super':
        index = randint(0, superheroes_len-1)
    elif fight_team == 'villains':
        index = randint(0, villains_len-1)
    return index


def get_hero_and_villain_for_match(random_hero_index, random_villain_index) -> list[character]:

    hero = get_superhero(random_hero_index)
    villain = get_villain(random_villain_index)

    attackers: list[character] = [hero, villain]
    return attackers


def perform_attact_calculations(hero, villain) -> list:
    heros_life: int = 0
    villain_life: int = 0
    # Perform the attacking calculations
    # Add the hero and villain powers to the life
    heros_life += hero['life']
    villain_life += villain['life']

    # subtract the life's of each oponent from the other
    heros_life -= villain['attack_power']
    villain_life -= hero['attack_power']

    final_lifes = [heros_life, villain_life]
    return final_lifes


def check_for_winner(heros_life, villain_life) -> None:
    """Checks to see who's power is greater than the other """
    WIN_MESSAGE: Final[str] = "You successfully saved Zortan!!!. "
    lOOSE_MESSAGE: Final[str] = "Thanos killed Avengers and captured Zortan!!"
    if heros_life > villain_life:
        print(WIN_MESSAGE)
    else:
        print(lOOSE_MESSAGE)


def attack():

    for i in range(3):
        random_hero_index = get_random_indexes('super')
        random_villain_index = get_random_indexes('villains')
        hero, villain = get_hero_and_villain_for_match(
            random_hero_index, random_villain_index)
        print(f"Heros : {hero}")
        print(f"Villain : {villain}")
        # Perform the actual attack calculations
        heros_life, villain_life = perform_attact_calculations(hero, villain)

    check_for_winner(heros_life, villain_life)


def main():
    attack()


if __name__ == "__main__":
    main()
