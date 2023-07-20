# JSON: JavaScript Object Notation: Python comes with tools already to deal with this type of data

# Equivalence Python to JSON format:
# PYTHON --- JSON
# dict ---------------- object
# list, tuple --------- array
# str ----------------- string
# int, long, float ---- number
# True ---------------- true
# False --------------- false
# None ---------------- null

# Lets say we have a python dictionary and we want to convert it to JSON format:

import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

personJSON = json.dumps(
    person, indent=4, sort_keys=True
)  # Will convert our dictionary into JSON format, can also set up an amount of indentation spaces, usually 4 for better visualization, we can also choose to order our keys vertically
print(personJSON)

# This allows us to create a JSON file and save some values to it
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Convert JSON data into Python dictionary (Converting from JSON to our format is also called Deserialization)
with open("person.json", "r") as file:
    person = json.load(file)
    print("Heres the ")
    print(person)

# More examples


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User(
    "Max", 27
)  # Class instances are not valid yet for transforming into JSON format, it will give an error, so we gotta encode it with a function into a new object


def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJSON = json.dumps(
    user, default=encode_user
)  # Overwrite default encoding function to encode with our new function

# Another way to create a custom JSON encoder
from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


# We can then use it like this:
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# or in this shorter version:
userJSON = UserEncoder().encode(user)
print(userJSON)

# Another way to convert JSON into dictionary
user = json.loads(userJSON)


# but again we need to decode it first to actually access its properties, otherwise user["name"] would give us an error
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


# Now its properties are accessible to read
user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
