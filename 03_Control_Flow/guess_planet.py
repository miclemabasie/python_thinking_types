"""
Friends from Earth wnat to know were is Louis,so Louis decides to
Write a program that will make them guess the name of planet
"""

guess: str = ""
my_planet_name: str = "Zortan"

while guess != my_planet_name:
    guess = input("Please Guess the name of my planet: ")
    # print(guess)
    guess = guess.capitalize()
    print(guess)
    if guess == my_planet_name:
        print("Yeahh! you guessed it!")
    else:
        print(f"Louis says: {guess} is not my planet name.")

while True:
    guess = input("Please Guess the name of my planet: ")
    # print(guess)
    guess = guess.capitalize()
    print(guess)
    if guess == my_planet_name:
        print("Yeahh! you guessed it!")
        break
    else:
        print(f"Louis says: {guess} is not my planet name.")
