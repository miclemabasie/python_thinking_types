# String: ordered, immutable, text representation

mystring = "Hello World!"

# convert to upper
mystring.upper()

# check first charaters
mystring.startswith("H")

#check last characters
mystring.endswith("world")


# count number of letters in a string
mystring.count("o")

# replace parts of the string
new = mystring.replace("world", "There")

mystring = "how are you doing"

# turn string into list
mylist = mystring.split()

# turn list into a string
" ".join(mylist)

var = "Tom"
fl = 3.3333
integer = 34
string = "The variable is %s" %  var
string = "The integer is %d" %  integer
string = "The Float is %s" %  fl

# using the format method

string = "The complete string is: str: {}, fl: {:.3f}, int: {}".format(var, fl, integer)

# using fstrings
string = f"The complete string is: str: {var}, fl: {fl}, int: {integer}"
