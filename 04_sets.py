# Sets are like lists or tuples in a way, but they are and generate completely unordered / randomised order, they are mutable, but they dont allow duplicates
# If we manually enter duplicates, it will not give error but will simply remove any additional duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

# Another way to create a set based on a given list
myset = set([1, 2, 3])
print(myset)

# We can also use sets to find the length of a given word, since it will just separate each of the letters
myset = set("Hello")
print(len(myset))

# Create an empty set (we add things to it later on)
myset = set()

# Add some values to the set
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Remove some value from the set, will create an error if it doesnt find it
myset.remove(1)
print(myset)

# Another way to remove some value from the set, but this time it will not create an error if it doesnt find it
myset.discard("hello")
print(myset)

# Clear a entire set
myset.clear()
print(myset)

# Pop will remove the last value of a set, but since the last value position will be an arbitrary value, it will remove random value each time
myset = {"hello", 1, 2, 3, "goodbye"}
myset.pop()
print(myset)
myset.pop()
print(myset)

# Loop a set
for item in myset:
    print(item)

# Check if a given value exists on a set:
if 2 in myset:
    print("found a 2")

# Working with different sets: Odds, evens and primes
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Merge sets together without repeating any values ever
union_set = odds.union(evens)
print(union_set)

# Create a set based on values that are repeated among 2 different sets
intersection_set = odds.intersection(primes)
print(intersection_set)

# Create a set based on values that are on the first set but not in the second set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff_set = setA.difference(setB)
print(diff_set)


# Symetric difference: Create a set based on values that are in a set but not repeated in the other
symetric_diff_set = setA.symmetric_difference(setB)
print(symetric_diff_set)

# Merge 2 sets together
setA.update(setB)
print(setA)

# Intersection update: Update a set based on values that are repeated in both sets
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.intersection_update(set2)
print(set1)

# Difference update: Remove all values from a set that are present within another given set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)

# Symetric difference update: Update a set by keeping values that are in any of the sets but not repeated in the other
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(set1)

# Subsets: Check and returns True if all the elements of our first set are also in the second set, otherwise False
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set2.issubset(set1))

# Supersets: Subsets but the other way around: Check and returns True if all the elements of the second set are present in the first set, otherwise False
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1.issuperset(set2))

# Disjoint: Check if any of the values of the second set are not repeated on the first set, if so returns True, otherwise returns False
set1 = {4, 5}
set2 = {1, 2, 3}
print(set1.isdisjoint(set2))

# Frozen set: Create an immutable set
set1 = frozenset([1, 2, 3, 4])
print(set1)
# set1.add(5) # Error
# set1.remove(1) # Error
