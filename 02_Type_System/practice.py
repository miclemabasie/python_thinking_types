""".mypy_cache/
    Louis wants to open a Pizza shop and needs to wrie
    a program for acceptiong orders.

    Tip -
    -----
    Always visualize First, Then Start Coding.
"""
# -------------------------------------------
# Variable Declaration
# -------------------------------------------

customer: str = "Miclem"
pizza_base: str = "thin"
pizza_size: int = 12
topping: str = "Olives"
extra_cheese: bool = True
price: float = 8.99

# -------------------------------------------
# Alternative 1 - Using Print Function
# -------------------------------------------

print(f"Received order from: {customer}")
print(
    f"Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}")
print(f"Pizza Price: {price}")

# -------------------------------------------
# Alternative 2 - Using Formatted Strings
# -------------------------------------------

order_output: str = f"""
Received Order From: {customer}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
Pizza Price: {price}
"""
# print(order_output)

name = input("Please Enter a customer name: ")
price = input("Pleas enter the pizza's price: ")

order_output = """
    Received Order From: {},
    Pizza Base: {},
    Pizza Size: {} inches,
    Pizza Topping: {},
    Pizza price: ${}
""".format(name, pizza_base, pizza_size, topping, price)

print(order_output)
