# Errors and Exceptions: Errors and Exceptions will cause the program to stop executing further
# Most common errors with examples:

# SyntaxError (cannot write the variable and the print on the same line)
# a = 5 (print(a))

# TypeError (cannot sum together an int and a str)
# a = 5 + "10"

# ModuleNotFound (must import available modules, not an invented name like in the example below)
# import somemodule

# FileNotFoundError (same thing as above but with Files instead)
# f = open("somefile.txt")

# ValueError (the value 4 is not in the list)
# a = [1, 2, 3]
# a.remove(4)

# KeyError: age is not in the provided dictionary
# my_dict = {"name": "Max"}
# my_dict["age"]

# Create an exception manually when a given condition is met
# x = -2
# if x < 0:
#     raise Exception("x should be positive")

# Alternative way: Assert (asset will raise an exception AssertionError if the given condition is not True)
# x = -5
# assert x == 0

# We can also provide a description about the error as a second parameter
# x = 3
# assert x == 0, "x is not a 0"

# Catch exception with try / except
# try:
#     a = 5 / 0  # will throw a ZeroDivisionError
# except Exception:
#     print("an error happened")

# We can also capture the error within the except
# try:
#     a = 5 / 0
# except Exception as e:
#     print(f"the exception error description is: {e}")

# If we are expecting a certain type of error in order to do some action, we can also except for specific errors
# try:
#     a = 5 / 1
#     b = a + "10"
# except ZeroDivisionError as e:
#     print("thats a zero division error")
# except TypeError as e:
#     print(f"got a typeerror: {e}")

# We can do an else in case no exceptions are raised
# try:
#     a = 5 / 3
#     b = a + 2
# except ZeroDivisionError:
#     print("thats a zero division error")
# except TypeError:
#     print("got a type error there")
# else:
#     print("everything execute without any errors")
# finally:
#     print(
#         "this will execute regardless of exceptions being raised or not, often used to reset something to initial values, for example"
#     )


# We can also create our own exceptions by subclassing from the BaseError class:
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")


try:
    test_value(200)  # Will output ValueTooHighError: value is too high
except ValueTooHighError as e:
    print(e)


# We can also create more customised, detailed errors
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x < 5:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(3)
except ValueTooSmallError as e:
    print(e.message, e.value)
