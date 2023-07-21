# Decorators: wrapper that modifies the behavior of a function or method without changing its source code, typically used for adding common functionalities like logging or timing.


def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def print_name():
    print("Alex")


print_name()  # Will print "Alex"
print_name = start_end_decorator(print_name)
print_name()  # Will print "Start" then "Alex" then "End"


@start_end_decorator  # This is the decorator pattern, is another way to do the same as we just did before, this will also print "Start" then "Alex" and then "End"
def print_name():
    print("Alex")


print_name()


# This one will give a TypeError: start_end_decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given
# @start_end_decorator
# def add5(x):
#     return x + 5
# add5(10)


# We modify the wrapper so that it can receive arguments:
def start_end_decorator(func):
    def wrapper(
        *args, **kwargs
    ):  # As many arguments and keyword arguments as we want to use
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_end_decorator
def add5(x):
    return x + 5


# Now it will not give error anymore
result = add5(10)
print(result)


# Repeat Decorator by passing arguments
import functools


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Miguel")


# Decorators can be stacked on top of another

# @decorator1
# @decorator2
# @decorator3
# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting

# say_hello("Pepe")


# Class-based decorators are also possible, not only function decorators. Class decorators are used to "remember" (in memory) some value everytime the function executes.


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(
        self, *args, **kwargs
    ):  # Built in class method that will execute everytime we call an instance of the class
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")


cc = CountCalls(
    None
)  # Create an instance of the CountCalls class, we should usually pass a function in this case but we pass None because it doesnt matter for the example
cc()  # This will execute the __call__ from CountCalls


# We implement the class instance Decorator:
@CountCalls
def say_hello():
    print("Hello")


say_hello()  # Will print: "This is executed 1 times"
say_hello()  # Will print: "This is executed 2 times"
say_hello()  # Will print: "This is executed 3 times"
