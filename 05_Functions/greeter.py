"""
Functions:
==========

It's all about data transformation, ideally it should
`take something -> give something`.

Or sels, it causes a 'side effect'.

Remenber people in Zortan greet each other by saying Zola,
Louis wants to write a program which can greet any Zortan!
"""


def greet_zortan(name: str) -> None:
    print(f"Zola! {name}")


# greet_zortan('Abasie')


def main():
    friends: list[str] = ['Cece', 'Roko', 'Chiko', 'Niko', 'Ziko']

    for friend in friends:
        greet_zortan(friend)


if __name__ == '__main__':
    main()
