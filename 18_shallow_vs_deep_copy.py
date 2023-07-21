# Shallow copy: One level deep, only references of nested child objects
# Deep copy: Full independent copy
import copy

org = 5
cpy = org  # Not an actual copy, just a reference to the variable

# Make shallow copy:
cpy = copy.copy(org)

# Assuming org its a list now, we can do a shallow copy like this as well:
org = [1, 2, 3, 4]
cpy = org[:]

# Make a deep copy
org = [1, 2, 3, 4]
cpy = copy.deepcopy(org)


#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Shallow copy of a class instance
p1 = Person("Alex", 27)
p2 = copy.copy(p1)
