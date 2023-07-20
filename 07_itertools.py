# Iterators are data structures that could be looped with a for: lists are the most common iterators

# Product: Will iterate over the values of multiple iterators
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod)  # iterable, convert it into a list to see its data
print(list(prod))

# Permutations: Will return all possible orders of a given input
from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

# Combinations: Will return all possible combinations without repeating characters, given the length as secondary parameter
from itertools import combinations

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

# Combinations with replacement: Will return all possible combinations including repeating characters, given the length as secondary parameter
from itertools import combinations_with_replacement

comb_with_replacement = combinations_with_replacement(a, 2)
print(list(comb_with_replacement))

# Accumulate functions: It will accumulate the sum of values on each iteration
from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

a = [1, 2, 6, 3, 4]
acc = accumulate(
    a, func=max
)  # Func max will returns the highest value found on each iteration, based on all previous iterations and current one
print(list(acc))

# GroupBy: Will separate datastructures into subsets based on a specified condition
from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

# More realistic example of a groupby

persons = [
    {
        "name": "Tim",
        "age": 25,
    },
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]


def specific_age(x):
    return x["age"]


group_obj = groupby(persons, key=specific_age)
for key, value in group_obj:
    print(key, list(value))

# Count, Cycle, Repeat functions
from itertools import count, cycle, repeat

# Count: Will start a loop at the provided number
for item in count(10):
    print(item)
    if item == 15:
        break

# Cycle: Will indefinitely cycle through an iterable
a = [1, 2, 3, 4]
for item in cycle(a):
    print(item)

# Repeat: Will make an infinite loop repeating a value over and over, also can be passed a second parameter to tell it how many times it will repeat / iterate over
a = [1, 2, 3, 4, 5, 6]
for item in repeat(a, 2):
    print(item)
