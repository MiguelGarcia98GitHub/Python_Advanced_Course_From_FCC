# Generator: Special type of function that returns an iterable sequence of results, lazily on demand (one at a time), instead of computing all results at once. This makes them highly memory efficient when dealing with large data streams.
def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

# Can be looped over
# for item in g:
#     print(item)


value = next(g)  # will return 1
print(value)
value = next(g)  # will return 2
print(value)
value = next(g)  # will return 3
print(value)
# value = next(g)  # will create an error with StopIteration (we already consumed all yields on the generator)
# print(value)


# Will return
def mygenerator():
    yield 1
    yield 2
    yield 1


g = mygenerator()
sorted_g = sorted(g)  # Can be sorted
print(sorted_g)


#


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)  # Will not print "Starting"

value = next(cd)  # This will print "Starting", and return a 4
print(value)
value = next(cd)  # This will print "Starting", and return a 3
print(value)
value = next(cd)  # This will print "Starting", and return a 2
print(value)


# This is a manually created attempt to create a generator without using a generator, this would actually work but will consume a huge amount of memory
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


mylist = firstn(10)
print(mylist)


# Same as above but using an actual generator, much more efficient in terms of memory, also less code
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn(10)))
print(sum(firstn_generator(10)))


# Fibonacci example using generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for item in fib:
    print(item)
