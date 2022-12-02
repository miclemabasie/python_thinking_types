"""
Gravity works differently in Zortan, use the following formula
to see hwo much you weigh on zortan.

Zortan weight = (Earth weight + 32) / 8
"""


def calc_weight(weight: float) -> float:
    """Perform weight calculations"""
    zortan_weight = (weight + 32) / 8
    return zortan_weight


def main():
    my_weight = calc_weight(75)
    print("Your weight is: {:.5f}Kg in Zortan".format(my_weight))
    print(f"Your weigh is {my_weight:.2f} Kg in Zortan.")


if __name__ == '__main__':
    main()
