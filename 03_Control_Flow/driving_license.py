"""
Louis wants to drive a car and wants to know if he can
apply for a driving license or not.
"""
# user_age = int(input("Enter you age: "))
age: int = 13


def check_valid_age(age):
    if age < 16:
        print("You are not eligible for a License")
    else:
        print("You are eligible for License.")


# ------------------------------------
# If / Else Statement
# ------------------------------------
# if age < 16:
#     print("You are not eligible for a License")
# else:
#     print("You are eligible for License.")
# ------------------------------------
# After a couple of years.
# ------------------------------------
age = 19
# if age < 16:
#     print("You are not eligible for a License")
# else:
#     print("You are eligible for License.")


# ------------------------------------
# Alternative Implementation - Without 'Else' block
# ------------------------------------
if age < 16:
    print("You are not eligible for a license.")
print("You are eligible for a license.")

# ------------------------------------
# After too may years
# ------------------------------------
age = 100
if age < 16:
    print("You are not eligible for a License")
elif age >= 80:
    print("You are too old to get a License")
else:
    print("You are eligible for a License.")
