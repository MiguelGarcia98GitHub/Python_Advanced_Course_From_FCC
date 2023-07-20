# Random numbers: Python comes with some modules for generating random numbers
import random

a = random.random()  # will print a random float between 0 and 1
print(a)

# We can change this 0-1 range by using random.uniform
a = random.uniform(1, 10)
print(a)

# Generate random int
a = random.randint(1, 10)
print(a)

# For statistics: It will pick a random value based on the Gaussian distribution, being the first parameter the mu, the mean or center of the distribution, and sigma the width of the distribution
a = random.normalvariate(0, 1)

# random.choice to select a random value from a non-empty list
my_list = list("ABCDEFGH")
print(my_list)
a = random.choice(my_list)
print(a)

# random.sample is similar but will also receive an argument of the amount of unique elements we want to get
a = random.sample(my_list, 3)
print(a)

# If we want to do this same behaviour but while allowing for non-unique members as well we can do random.choices
a = random.choices(my_list, k=3)
print(a)

# random.shuffle it will randomly move the elements around
random.shuffle(my_list)
print(my_list)

# Randomise but using a specific start seed, meaning upcoming values are expected to be predictable, following examples would produce same outputs everytime
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# Seed should not be exposed then, for security reasons, we can use secrets module for that (also used for security tokens, auth... etc)
import secrets

a = secrets.randbelow(10)
print(a)
a = secrets.randbits(4)
print(a)

# Truly generate random values without those values being reproducible
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

# Often for professional mathematical operations and working with large amount of data its used the popular module NumPy, we can install it with pip install NumPy. NumPy makes mathematical operations faster and better
import numpy as np

# Create truly randomised values using numpy
np.random.seed(1)
a = np.random.rand(3)  # Creates 1 dimensional array with random 0-1 float on each space
print(a)
a = np.random.rand(
    3, 3
)  # Creates array with 3 arrays each containing 3 of 0-1 float values
print(a)

# If we want to have integers instead:
a = np.random.randint(0, 10, 3)  # Range 0 to 10 and amount of values to generate
print(a)
