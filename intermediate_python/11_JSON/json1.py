import json
# name, age, city, hasChildren, titles = []
person = {"name": "python-Enginer", "age": 55, "city": "Boston Masechesetes", "hasChildren": True, "titles": ["SW Engineer", "Programmer"]}

# json.dumps conver a simple python dictionary object into json datatype
# json output can be sorted with 'sort_key=True parameter
personJson = json.dumps(person, indent=4)

# convert dictionary into json and put content in a file "json.dump"
with open("./person.json", "w") as file:
    json.dump(person, file, indent=4)

# Convert JSON object to a python dictionary (Decoding or Deserialization)
newperson = json.loads(personJson) # dumps -> Dump string
print(newperson)

# Conver JSON object to a python dictionary from a file
with open("./person.json", "r") as file:
    personJson2 = json.load(file)
    print(personJson2)

