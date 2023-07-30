# Dictionary: key-value-pair, Unordered, Mutable

mydict = {"name": "Miclem", "age": 30, "city": "New York"}
print(mydict)

# Using the dict function

dict1 = dict(name="Abasie", age=30, city="Boston")

# Accessing values from the dictionary

value = dict1["name"]

value = dict1["lastname"] # Exception -> KeyError


# update the dictionary:
mydict["email"] = "miclema@mail.com"
print(mydict)

# Delete items from the dictionary
del mydict["email"]
print(mydict)


