"""
Save Zortan:
------------

The war has just intensified, Thanos army has reach Zortan and are going to 
fight along with him. With his army, this time Thanos is going to attack Ave
and the battle is going to be intense!!!

Since, everthing is going in real-time, we don't have control over characters
instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters. so as we
can see out code is geeting better and certainly we are going to make it better 
as we progress with future modules
"""
from typing import Final
import random


character = dict[str, str | int]

# Super Heroes
IRONMAN: Final[character] = {
    'name': 'Ironman', 'attack_power': 250, 'life': 100}
BLACKWIDOW: Final[character] = {
    'name': 'BlackWidow', 'attack_power': 180, 'life': 800}
SPIDERMAIN: Final[character] = {
    'name': 'SpiderMan', 'attack_power': 190, 'life': 700}
HULK: Final[character] = {
    'name': 'Hulk', 'attack_power': 300, 'life': 1100}

# Super Villains
THANOS: Final[character] = {
    'name': 'Thanos', 'attack_power': 1500, 'life': 1500}
REDSKULL: Final[character] = {
    'name': 'RedSkull', 'attack_power': 300, 'life': 800}
PROXIMA: Final[character] = {
    'name': 'Proxima', 'attack_power': 320, 'life': 800}

WIN_MESSAGE: Final[str] = "You successfully saved Zortan!!!. "
lOOSE_MESSAGE: Final[str] = "Thanos killed Avengers and captured Zortan!!"


# All Super Heros & Super Villains
superheros: list[character] = [IRONMAN, BLACKWIDOW, SPIDERMAIN, HULK]
supervilains: list[character] = [THANOS, REDSKULL, PROXIMA]

hero_life = 0
villlain_life = 0

# will run the loop for the number of times specified in the range function
for attack in range(3):
    hero_attack_index: int = random.randint(0, 3)
    villain_attack_index: int = random.randint(0, 2)

    # Get the hero to attack at the moment based on the index
    # that was randomly selected from the heros list, similarly with the villain
    current_attacking_hero = superheros[hero_attack_index]
    attacking_villain = supervilains[villain_attack_index]

    # Adding the life
    hero_life += current_attacking_hero['life']
    villlain_life += attacking_villain['life']

    # Attack
    hero_life -= attacking_villain["life"]
    villlain_life -= current_attacking_hero['life']

    print(
        f"Attack: {attack+1} => {current_attacking_hero['name']} is going to fight with {attacking_villain['name']}")

# Get some space
print('*' * 50)

if villlain_life > hero_life:
    print(lOOSE_MESSAGE)
else:
    print(WIN_MESSAGE)
