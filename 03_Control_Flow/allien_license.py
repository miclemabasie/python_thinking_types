"""
Louis wants to drive a car and he hears that in planet
Zortan there is not age limit for getting a license

'AND' Table
-----------
True and True => True
False and False => False
True and False => False
False and True = False

'OR' Table 
----------
True or True => True
False or False = False
True or False = True
False or True = True
"""

age: int = 10
planet: str = "Earth"
# -------------------------------------
# And / OR Statements
# -------------------------------------


if age < 16 and planet == "Earth":
    print("You are NOT eligible for a license on Earth")
elif age > 6 and planet == "Earth":
    print("You can apply for a license on Earth")
elif age < 16 or planet == "Zortan":
    print("You can apply for a Zortanian License!!")

# -------------------------------------
# Louis migrates to Zortan
# -------------------------------------
planet = "Zortan"
if age < 16 and planet == "Earth":
    print("You are NOT eligible for a license on Earth")
elif age > 6 and planet == "Earth":
    print("You can apply for a license on Earth")
elif age < 16 or planet == "Zortan":
    print("You can apply for a Zortanian License!!")
