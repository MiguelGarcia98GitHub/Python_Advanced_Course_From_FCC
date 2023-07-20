# Dictionaries are similar to objects in other programming languages or JSON, basically key-value pairs.
# In Python they are usually called by their abbreviation: dicts

# Create a dict
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Another way to create a dict
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Get the value of the given key
value = mydict2["name"]
print(value)

# Create a new key-value pair or overwrite the value if already exists
mydict2["email"] = "mary@xyz.com"
print(mydict2)
mydict2["email"] = "mary123@xyz.com"
print(mydict2)

# Delete a specific key-value
del mydict2["name"]
print(mydict2)

# Another way to delete a specific key-value
mydict2.pop("age")
print(mydict2)

# This is an (older and less used) way to delete the last inserted key-value pair
mydict2.popitem()
print(mydict2)

# Check if a key exists:
if "city" in mydict2:
    print(mydict2["city"])

# Another way to check if a key exists
try:
    print(mydict2["name"])
except:
    print("Error, name wasnt found as a key on the given dictionary")


# Print all the keys of a given dict:
mydict3 = {"name": "Pepe", "email": "pepe@xyz.com", "age": 40}
for key in mydict2:
    print(key)

# Another way (and more clear) to loop through the keys of a dict:
for key in mydict3.keys():
    print(key)

# Loop through the values instead:
for value in mydict3.values():
    print(value)

# Loop through both keys and values at the same time:
for key, value in mydict3.items():
    print(key, value)

# Copy a dictionary into a new one:
dict_copy = mydict3.copy()
print(dict_copy)

# Merge a dictionary into another (if some key-value pairs already exist those will remain unchanged)
mydict3.update(mydict2)
print(mydict3)

# Dict with numeric keys:
mydict4 = {3: 9, 6: 36, 9: 81}
print(mydict4)

# But in this case index search will not work anymore like with strings:
# value = mydict4[0] - This will throw error, because it will try to find the numeric value of 0, but theres only 3,6 and 9

# To find the values this way, we use the actual numeric value of the key:
value = mydict4[3]
print(value)

# A tuple could also be inserted as a dictionary key (but lists cannot be used as keys, that is basically because a list is not hashable because it can be modified later on, unlike sets)
mytuple = (8, 7)
mydict5 = {mytuple: 15}
print(mydict5)
