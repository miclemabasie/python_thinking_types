"""
Functions:
==========

Think in data transformations
`take something -> give something`.

Delegate handling responsibility to the caller function.

Tip:
====
Very useful pattern for testing!!!
"""

# Returns a greeting message to caller function
# Caller function decides what to do with the response


def greet_person(name: str) -> str:
    """Greets Zortan"""
    # Greeter 'transforms' the original string into something useful
    # ant returns it.
    return f"Zola {name}"
# print(f"Hi {name}, You are welcome aboard!.")


# Main acts as the caller function for gree_person
# It can handle the response in multiple ways
def main() -> None:
    friends: list[str] = ['Cece', 'Roko', 'Chiko', 'Niko', 'Ziko']
    # Loop through the list of friends
    for friend in friends:
        greet = greet_person(friend)
        if 'Roko' not in greet:
            print(greet)


# invoke the main function
if __name__ == '__main__':
    print("Running the main function.!!")
    main()
