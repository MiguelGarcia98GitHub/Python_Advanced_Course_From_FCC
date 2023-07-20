# Collections: Special container data types, provides alternatives with additional functionalities to data structures like tuples or dictionaries.
# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter: Container that stores the elements as dictionary keys and their counts as dictionary values
from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())

# Get the most common element of the counter
print(my_counter.most_common(1))

# Get the two most common elements of the counter
print(my_counter.most_common(2))

# Get all elements from the counter
print(list(my_counter.elements()))


# Create a new subclass of tuple with named fields
from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# Ordered Dict
# An ordered Dict is like a dictionary but order will be remembered
from collections import OrderedDict


ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)

# Default Dict
# Like a dictionary but if a key doesnt have a value assigned yet it will have a default value instead
from collections import defaultdict

default_dict = defaultdict(int)  # default type as int in this example
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict)
print(default_dict["a"])
print(default_dict["b"])
print(
    default_dict["c"]
)  # will give an int type, a 0 actually because 0 is the default of an int type, if it would be a float then 0.0, etc


# Deque
from collections import deque

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)  # will add to the left side
print(d)
d.pop()  # remove the last element
print(d)
d.popleft()  # remove the first element
d.extend([4, 5, 6])  # add elements to the right side
d.extendleft([4, 5, 6])  # add elements to the left side, in reverse order
print(d)
d.rotate(
    1
)  # will rotate all elements the given number amount of times to the right, being 1 in this example
print(d)
d.rotate(
    -1
)  # if we use a negative items it will rotate all elements 1 place to the left
