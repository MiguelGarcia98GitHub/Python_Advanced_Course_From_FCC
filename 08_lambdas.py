# Lambdas are small anonymous functions that are defined without a name, first it has the lambda keywords, then can have some arguments, then a : and then an expression
add10 = lambda x: x + 10

print(add10(5))

multiple_args = lambda x, y: x * y
print(multiple_args(2, 7))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)

# map function: Takes a function as an argument that will apply to every item of the iteration and then an iterable as a second argument
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

# filter function: Takes a function as an argument that will evaluate to true or false and if true will allow the item to pass the filter, then the iterable as a second argument
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x > 3, a)
print(list(b))


# reduce function: Also takes a function and an iterable and it repeatedly applies the function to the elements and ends up returning a single value
from functools import reduce

a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
