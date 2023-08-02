# Map applies a function to every element in a collection
# Filter: Filters out element in a collection based on a conditions specified in a function
# Reduct: Returns a single value based on the input function logic bu taking in a function and a collection 
# Sorted: sorts elements in a list

# The above functions are the ones that are typically used with the lambda syntax
from functools import reduce

points = [(3, 7), (2, 4), (0, 15), (9, 2), (10, 6)]

s = sorted(points, key=lambda x: x[0] * x[1])

mylist = [1, 2, 3, 4, 5, 6, 7]
m = map(lambda x: x * x, mylist)
print(list(m))

f = filter(lambda x: x%2==0, mylist)
print(list(f))

# Reduce
r = reduce(lambda x,y: x * y, mylist)
print(r)