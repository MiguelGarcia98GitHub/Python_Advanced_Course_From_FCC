# Create a list
mylist = ["banana", "cherry", "apple"]
print(mylist)

# Create an empty list
mylist2 = list()
print(mylist2)

# Lists can have different value types and also similar values at the same time
mylist3 = [5, True, "apple", "apple"]

# Access the element at given index in the list, will give error if we give it an index value bigger or equal to the list length
item = mylist[2]
print(item)

# Access elements at given negative index, starting from the end
item_with_negative_index = mylist[-1]
print(item_with_negative_index)

# Iterate over a list, the name we give it between the "for" and "in" will be the name of the variable for each loop, its often seen as i but could be anything like item or x or any other word
for item in mylist3:
    print(item)

# Find if theres a specific value on a list
mylist4 = ["car", "plane", "boat", {"vehicle": "motorbike"}]
if "car" in mylist4:
    print("car found")  # will execute this

if {"vehicle": "motorbike"} in mylist4:
    print("vehicle motorbike found")  # will execute this

if "somerandomvalue" in mylist4:
    print("somerandomvalue found")
else:
    print("not found somerandomvalue")  # will execute this

# Check the length of a given list
list_length = len(mylist4)
print(list_length)

# Add a value at the end of the list
mylist5 = ["a", "b"]
mylist5.append("c")
print(mylist5)

# Insert a value at a given index
mylist6 = ["fish", "meat", "vegetables", "milk"]
mylist6.insert(2, "multivitamins")
print(mylist6)

# Removes the last item and returns it
mylist6.pop()
print(mylist6)

# Remove a specific element based on its value, will give ValueError if value is not found
mylist7 = ["dog", "cat", {"rodent": "hamster"}]
mylist7.remove("dog")
mylist7.remove({"rodent": "hamster"})
print(mylist7)

# Clear an entire list
mylist8 = ["a", "b", "c"]
mylist8.clear()
print(mylist8)

# Reverse a list
mylist9 = ["a", "b", "c"]
mylist9.reverse()
print(mylist9)

# Sort a list, alphabetically or numerically, but not both together, or it will create a TypeError like this: '<' not supported between instances of 'int' and 'str'
mylist10 = ["f", "car", "b", "a"]
mylist10.sort()
print(mylist10)
mylist11 = [34, 46, 12, 87]
mylist11.sort()
print(mylist11)

# Create a new list from another list and sorts the new list
mylist12 = ["car", "plane", "boat"]
sorted_mylist12 = sorted(mylist12)
mylist12.append("motorbike")
print(sorted_mylist12)

# Create a new list the desired amount of repited items
mylist13 = ["hello"] * 5
print(mylist13)

# Create a new list based on already existing multiple lists
mylist14 = mylist13 + mylist12 + mylist11
print(mylist14)

# Create a new list based on a specific part of another list (specifying which index we start at and which index we end at, but end index is exclusive so actually just the index before that one)
mylist15 = [10, 27, 30, 43, 50, 67, 75, 80, 95]
new_list_15 = mylist15[1:5]
print(new_list_15)

# If we dont specify a start index then it will start from the beginning, at index 0
from_beginning_new_list15 = mylist15[:3]
print(from_beginning_new_list15)

# And if we dont specify a end index then it goes all the way to the end
until_the_end_new_list15 = mylist15[2:]
print(until_the_end_new_list15)


# Copying a list (creating a new list, so we are not modifying old one when changing values)
mylist16 = ["banana", "cherry", "apple"]
copy_mylist16 = list(mylist16)
print(copy_mylist16)
another_copy_mylist16 = mylist16[:]
print(another_copy_mylist16)

# List comprehension: Create a new list based on an already existing list while getting the new values based on a modification of the old values, for example get the squared values
mylist17 = [1, 2, 3, 4, 5, 6]
list_comprehension_new_mylist17 = [item * item for item in mylist17]
print(list_comprehension_new_mylist17)

# Another example of list comprehension
mylist18 = ["1", "2", "3", "4", "5"]
list_comprehension_new_mylist18 = [int(item) for item in mylist18]
print(list_comprehension_new_mylist18)
