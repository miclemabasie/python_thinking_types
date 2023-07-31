# List in Python

A list is a collection of one or more datatypes enclosed in [] and separated by commas

## Key things to note about a list in python.

* A list can contain different datatypes
* A list is mutable, which means it can be change or modified after it's creation
* A list is accesses index notation starting at zero e.g mylist[0] gives you the first item in the list

# Get the len of the list
print(len(mylist))

# add item at the end of a list
mylist.append("lemmon")

# insert item at a particular index
mylist.insert(1, "mangoes")

# remove the last item and returns it
mangoes = mylist.pop("mangoes")
                      
mylist.sort() # sorts in place -> changes the original list

newList = sorted(mylist) # Does not modify the original list

nlist = [0] * 5 # creates a new list with 5 zeros

mylist[1:3] # Gets all elements from index 1 to index 3
mylist[::-1] # reverses the list


# how ot deep copy a list
list1 = [1, 2, 3]
list2 = list1.copy()
list2 = list(list1)
list2 = list1[:]