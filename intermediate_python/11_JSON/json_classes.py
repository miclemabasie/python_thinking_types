import json

class User:

    def __init__(self, name, age, isEngineer):
        self.name = name
        self.age = age
        self.isEngineer = isEngineer


user = User("Max", 23, True)

# userJson = json.dumps(user)


# Create a custom encoding function

def convertUserToDict(user):
    if isinstance(user, User):
        print("The object is an instance of the class")
        dicUser = {"name": user.name, "age": user.age, "isEngineer": user.isEngineer}
        return dicUser 
        
    else:
        print("Not an instance of the class operations haulted")


userJSON = json.dumps(user, default=convertUserToDict)
print(userJSON)

