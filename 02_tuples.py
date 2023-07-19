# Tuples are similar to lists but cannot be modified after its creation, its ordered and immutable, and allows duplicate elements. Tuples are more efficient for large data

# The syntax of a tuple will often use () but it is not required, but the length must be longer than 1 or else we will have to use a "," and then empty right after, otherwise Python will believe its a string regardless of having () around or not having them
mytuple = ("Max", 28, "Boston")
print(mytuple)
mytuple_no_brackets = "Max", 28, "Boston"

not_recognised_as_a_tuple = "Max"
print(type(not_recognised_as_a_tuple))
neither_recognised_as_a_tuple = "Max"
print(type(neither_recognised_as_a_tuple))

recognised_tuple = ("Max",)
print(type(recognised_tuple))

# Another way to create a tuple
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# Get value of a specific index in the tuple, will give ValueError if given index is out of range
item = mytuple[0]
print(item)

# We cannot modify tuple values, will give TypeError
# mytuple[0] = "Tim"

# We can loop a tuple
for item in mytuple:
    print(item)

# We can check for a specific value in a tuple
if "Max" in mytuple:
    print("Max was found in our tuple")
else:
    print("he wasnt found")

# Check length of a tuple
letters_tuple = ("a", "p", "p", "l", "e")
print(len(letters_tuple))

# Count the amount of given value found
print(letters_tuple.count("p"))
print(letters_tuple.count("f"))

# Given a specific value, find its index (of the first instance it finds) (assuming it exists, if it doesnt exist we get a ValueError)
mytuple2 = ("Max", 28, 28, 28, "Boston")
print(mytuple2.index(28))
print(mytuple2.index("Max"))

# A list can be turned into a tuple and viceversa
mytuple3 = ("a", "b", "c", "d")
list_from_tuple3 = list(mytuple3)
print(list_from_tuple3)
tuple_from_list = tuple(list_from_tuple3)
print(tuple_from_list)

# Create a new tuple based on another tuple, and assign it 1 element every 2 elements of the base tuple
mytuple4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
one_every_two_tuple = mytuple4[::2]
print(one_every_two_tuple)

# Create a reversed tuple (one fast way to do so)
reversed_tuple = mytuple4[::-1]
print(reversed_tuple)

# Unpacking variables from a tuple
mytuple5 = "Max", 28, "Boston"
name, age, city = mytuple5
print(name)
print(age)
print(city)

# Unpacking multiple variables at once
mytuple6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i1, *i2, i3 = mytuple6
print(i1)  # 1
print(i2)  # everything in between the 1 and the 10 (in list format)
print(i3)  # 10

# Data Efficiency comparison: Tuples vs Lists (Tuples are more efficient for storing data, they are highly optimized)

import sys

example_tuple = (0, 1, 2, "hello", True)
example_list = [0, 1, 2, "hello", True]
print(sys.getsizeof(example_tuple), "bytes")  # 80 bytes
print(sys.getsizeof(example_list), "bytes")  # 104 bytes

# Time Efficiency comparison: Tuples vs Lists (Tuples are again more efficient and much much faster for its initial creation and reading data over)

import timeit

print(
    timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=10000000)
)  # Tuple takes 0.05 sec to loop over 10 million times
print(
    timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=10000000)
)  # List takes 0.21 sec to loop over 10 million times
