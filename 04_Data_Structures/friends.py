"""
List:
-----
Louis has been making good progress in Zortan and has make
new friends. All of them are meeting today and Louis wants
to write a program that can greet all of them.

In Zortan, People greet with saying "Zola"

Info:
-----
Lists are mutable data structures, that means the data inside might be mutated.
Index always starts from 0.
"""

# It's convenient to group all friends together using a List
# and then greet them

friends: list[str] = ["Cece", 'Roko', 'Chiko', 'Niko']
# List with Index No [   0,      1,      2,       3  ]

# ---------------------------------------------------
# Time to greet friends using a for-in loop
# ---------------------------------------------------

for friend in friends:
    print(f"Zola {friend}")


# ---------------------------------------------------
# Louis wants to count his number of friends
# ---------------------------------------------------

print(f"Friends Length: {len(friends)}")

# ---------------------------------------------------
# Louis had a fight with Niko and wants to unfrien him
# ---------------------------------------------------

unfriened = friends.pop()
# friends.remove('Niko')
# print(unfriened)

# ---------------------------------------------------
# Louis has made a new friend called Ziko (add)
# ---------------------------------------------------

friends.append('Ziko')
print(friends)

# ---------------------------------------------------
# Louis wants to check who is the 3rd friend in the list
# ---------------------------------------------------

print(friends[2])

# ---------------------------------------------------
# Oh-no Louis again had a fight, this time with Roko
# ---------------------------------------------------

friends.remove("Roko")

# ---------------------------------------------------
# Louis is now again friends with Roko
# ---------------------------------------------------

friends.insert(1, 'Roko')
print(friends)

# ---------------------------------------------------
# Louis wants to confirm if Roko is in the friends list
# ---------------------------------------------------

if 'Roko' in friends:
    print("Yes I and Roko are back together!.")

# ---------------------------------------------------
# Louis patches things up with Niko and he becomes his no 1 friend
# ---------------------------------------------------

friends.insert(0, 'Niko')
print(f"Friends: {friends}")


# ---------------------------------------------------
# Louis wants to sort his friends in an alphabetical manner
# ---------------------------------------------------

friends.sort()
print(f"Friends: {friends}")


# ---------------------------------------------------
# Louis doesn't want this ordering and wants to reverse the order.
# ---------------------------------------------------

friends.reverse()
print(f"friends: {friends}")

# ---------------------------------------------------
# Remove Niko from the list again
# ---------------------------------------------------

unfriened = friends.pop(2)

print(f"Friends: {friends}")
