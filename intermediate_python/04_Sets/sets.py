# Sets: Unordered, mutable, no duplicates
string = "my name is miclem and i am a swe student in the university of bamenda"
myset = set(string.split())
print(string.split())
print(myset)


# # Some common methods
# s = set()
# s.add(1)
# s.add(2) # adding elements to the set

# # remove elements from the set
# s.remove(4) # returns an error if the element does not exist in the set
# s.discard(4) # Ignore the operation if the item is not found in the set

# s.pop() # Return and remove an arbitrary value from the set
# s.clear() # Clear the set

# Unions and Intersections
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}


# union odds and evens
u = odds.union(evens) # Add elements to odds from even that are mission in odds
# -> {1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection of odd and even
i = odds.intersection(evens) # Returns all the common elements in both sets 

# Get the difference of the 2 sets
sA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
sB = {1, 2, 12, 13, 14, 15, 16}

diff = sA.difference(sB)
print(diff)