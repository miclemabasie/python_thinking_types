"""
Variable Scope:
===============

Scopes can be 'Global' or 'Local'
"""
# Varaible shadowing

num = 10


def print_global_number(num: int) -> None:
    print(f"Global Number is: {num}")


def print_number():
    num = 20  # Local or function scope
    print(f"My local number is: {num}")


def int_number() -> int:
    # Explicit global declaration
    global num
    num += 2
    return num


def inc_local_num():
    new_num = num + 10
    print(new_num)


print_global_number(num)
print_number()
print(int_number())
inc_local_num()
