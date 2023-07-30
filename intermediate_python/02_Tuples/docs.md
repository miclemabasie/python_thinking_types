# Tuple: ordered, immutable, allows doplicate elements

mytup = (1, 2, 4, "string")
print(mytup)

# accessing tuple data at index
mytup[0] # -> 1
mytup[-1] # -> "string"

# Elements can not be changed in a tuple
# mytup[0] = "new value" # ItemAssignmentError

# slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a[2:4]

# unpacking
t = ("miclem", 30, "Bamenda")

name, age, city = t

print(name, age, city)


nums = (0, 1, 2, 3, 4, 5)

i1, i2, *i3 = nums

print(i1, i2, i3)