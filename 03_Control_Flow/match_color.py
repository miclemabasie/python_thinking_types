"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

'match' is a new operator introduced in Python 3.10
"""

fav_color = input("Enter you favorite color: ").lower()


match fav_color:
    case "black":
        print("Louis has a Black T-shirt.")
    case "red":
        print("Louis has red car.")
    case "yellow":
        print("Louis has a YELLOW shoe")
    case "green":
        print("Loius as a GREEN hat")
    case _:
        print("Louis has nothing that has you fav color.!")
