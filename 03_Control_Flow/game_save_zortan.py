"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------

Since Zortan is under attack, Louis calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan

1. Ironman
4. Black Widow
2. Spiderman
3. Hulk

Each avender has it's attacking power and they have to fight Thanos
to save Zortan

Avengers cna attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""

from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

WIN_MESSAGE: Final[str] = "You successfully saved Zortan!!!. "
lOOSE_MESSAGE: Final[str] = "Thanos killed Avengers and captured Zortan!!"
thanos_life: int = 1500
choice = 0
MESSAGE: Final[str] = f"""
====================================================================
Zortan is under attack, choose the pairs no. that will attack Thanos
--------------------------------------------------------------------
1) Ironman & Black Widow({IRONMAN_ATTACK_POWER + BLACKWIDOW_ATTACK_POWER})
2) Black Widow & Spiderman({BLACKWIDOW_ATTACK_POWER + SPIDERMAN_ATTACK_POWER})
3) Spiderman & Hulk({SPIDERMAN_ATTACK_POWER + HULK_ATTACK_POWER}) 
4) Hulk & Ironman({HULK_ATTACK_POWER + IRONMAN_ATTACK_POWER})
====================================================================
"""
combined_attack_power = 0


attack_num = 0

while True:
    # win /loose
    if thanos_life <= 0 and attack_num <= 3:
        print(WIN_MESSAGE)
        break
    elif attack_num >= 3:
        # loose
        print(lOOSE_MESSAGE)
        break

    print(MESSAGE)

    choice = int(input("Enter your attack choice (option): "))
    if choice == 1:
        attack_num += 1
        print("Ironman & Black widow are attacking Thanos")
        print(f"Number of chances left {3 - attack_num}")
        combined_attack_power = IRONMAN_ATTACK_POWER + BLACKWIDOW_ATTACK_POWER
        thanos_life = thanos_life - combined_attack_power
        print(thanos_life)
    elif choice == 2:
        attack_num += 1
        print(f"Number of chances left {3 - attack_num}")
        print("Black Widow & Spiderman are attacking Thanos")
        combined_attack_power = BLACKWIDOW_ATTACK_POWER + SPIDERMAN_ATTACK_POWER
        thanos_life = thanos_life - combined_attack_power
    elif choice == 3:
        attack_num += 1
        print(f"Number of chances left {3 - attack_num}")
        print("Spiderman & Hulk are attacking Thanos")
        combined_attack_power = SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        thanos_life = thanos_life - combined_attack_power
    elif choice == 4:
        attack_num += 1
        print(f"Number of chances left {3 - attack_num}")
        print("Hulk & Iron are attacking Thanos")
        combined_attack_power = HULK_ATTACK_POWER + IRONMAN_ATTACK_POWER
        thanos_life = thanos_life - combined_attack_power
