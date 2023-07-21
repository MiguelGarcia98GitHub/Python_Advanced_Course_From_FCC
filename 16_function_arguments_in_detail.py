def print_name(name):
    print(name)


print_name("Alex")  # Positional argument


def foo(a, b, c):
    print(a, b, c)


foo(1, 2, 3)  # Positional arguments
foo(a=1, b=2, c=3)  # Keyword arguments
foo(c=3, a=1, b=2)  # In keyword arguments the order does not matter
foo(
    1, c=3, b=2
)  # We can also mix them both, but in that case positional arguments must always go first, then keyword arguments


# *args and **kwargs: args are all positional arguments left, while keywords args are all keyword arguments left, kwargs are in dictionary format because of the key-value pairs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)
