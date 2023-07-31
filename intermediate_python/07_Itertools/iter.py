# Itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby
# Infinite iterators
from itertools import count, cycle, repeat
from operator import mul

# Product: Finds the cartesian product of a two sets (list)

a = [1, 2]
b = [3]

prod = product(a, b, repeat=2)
# print(list(prod))

# Permutaions: Returns all possible order of elements in an iterable
a = [1, 2, 3]
perm = permutations(a, r=2) # the r argument specifies how many elements are to be returned for each arrangement
# print(list(perm))


# Combinations: Returns the possible combinations of elements in an iterable
names = ["Abraham", "Jacob", "Zoomer", "Zack", "Micheal", "Michel", "Tony"]
com = combinations(names, r=4)
# print(list(com))
print(len(list(com)))

# Accumulate: returns the acculated sums by default of a list
a = [1, 2, 3, 4]
acc = accumulate(a)
acc = accumulate(a, func=max) # binary functions to modify how the accumulate functions work
acc = accumulate(a, func=mul)
# print(list(acc))


# find the sum of elements in a list using accumulate
s = list(acc)[-1]
print(s)

# Gropby: Groups items in a list according to a given creteria
people = [
    {"name": "Jacob", "age": 24},
    {"name": "Micheal", "age": 25},
    {"name": "Abraham", "age": 24},
    {"name": "Tony", "age": 22},
    {"name": "Zoomer", "age": 23},
]

def age(person):
    return person['age']

l = [1, 1, 2, 3, 4]

gb = groupby(people, key=age)

for k, v in gb:
    print(k, list(v))


# Infinite Iterators: Cycle, Count, Repeat
# Cycle -> Keeps going over a list of elements until a stop conditions is met
# Count -> Starts counting from a given point until a stop condition is met
# Repeat -> Keeps doing one thing for a certain number of time as provided in the arguments