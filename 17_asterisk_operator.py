# The * operator can be used for a variety of purposes

# Multiply
result = 5 * 7
print(result)

# To the power of
result = 5**7
print(result)

# Can be used to create lists, tuples or strings with repeated elements
zeros = [0] * 10
print(zeros)
some_var = (0, 1) * 10
print(some_var)
some_var = "AB" * 10
print(some_var)


# Capture the rest of arguments of a function
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7, eight=8)


# Limit allowed parameters of positional arguments, after the * will only allow for keyword arguments
def foo(a, b, *, c):
    print(a, b, c)


# foo(1, 2, 3, 4, 5)  # Will create a TypeError
foo(1, 2, c=3)  # Works fine


# Can also destructure a list with *
def foo(a, b, c):
    print(a, b, c)


my_list = (0, 1, 2)
foo(*my_list)
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}  # Can also pass it as keyword arguments by destructuring a dictionary, needs to use **
foo(**my_dict)
