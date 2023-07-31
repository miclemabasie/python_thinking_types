# Collections: Counter, namedtuple, OrderedDict, defauldict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaabbbbcccccccc"

mycounter = Counter(a)

print(mycounter)

mycounter.most_common() # returns the most commone elements in the list in descending order

# Named tuples
Point = namedtuple("Point", "x,y")
p = Point(1, 4)
p.x # -> 1
p.y # -> 


# OrderedDict
# Remember the order in which items were added to a dictionary in older versions of python < 3.6
# Note: in recent versions of python this is not needed because the built in dict() datatype has this feature

# DefualtDict
# semilar to the default dict() with the difference that it will have a defualt value if the key has not been set yet

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d["d"]) # returns 0, because d does not exist as key in the dictionary


# DEQUE
# Double ended queue, It can be used to add and remove elements from both ends

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()