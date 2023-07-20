# Strings: Chains of text
my_string = "Hello World"
print(my_string)

# Escape characters with \ or simply use double quotes with single quotes, or single quotes with double quotes
# my_string = 'I\'m a programmer'

# String over multiple lines
my_string = """Hello
World
"""
print(my_string)

# Or escape multiple lines
my_string = """Hello\
World
"""
print(my_string)

# Access the character of an specific index
my_string = "Hello World"
char = my_string[0]
print(char)

# Or access it from a negative index to start from the end
final_char = my_string[-1]
print(final_char)

# We cannot change the value at an index of a string
# my_string[0] = "h" # TypeError: 'str' object does not support item assignment
print(my_string)

# Create a substring
substring = my_string[0:5]
print(substring)

# Create a reversed string
reversed_string = my_string[::-1]
print(reversed_string)

# Concatenation
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name

# Loop through a string
for item in greeting:
    print(item)

# Check if a string contains a substring
if "llo" in greeting:
    print("llo is present on the given string")
else:
    print("llo is not present on the given string")

# Create a new string based on another string while removing the whitespaces on this newly created string
my_string = "     Hello World        "
strip_string = my_string.strip()
print(strip_string)

# Lowercase all characters of given string
my_string = "HELLO WoRlD"
print(my_string.lower())

# Check if a string starts / ends with some character or a combination of characters
my_string = "hello world"
print(my_string.startswith("h"))
print(my_string.startswith("hello"))
print(my_string.endswith("world"))
print(my_string.endswith("ld"))

# Check if a string contains a character or multiple characters,returns the lowest index if true otherwise returns -1 if doesnt find it
print(my_string.find("hello"))
print(my_string.find("h"))
print(my_string.find("e"))
print(my_string.find("this is not in the given string"))

# Count the number of substring it finds
print(my_string.count("o"))

# Replace a part of the string
print(my_string.replace("world", "universe"))

# Create a list of words based on a given string
list_based_on_string = (
    my_string.split()
)  # the default argument on split is a space, but can be modified to whatever we want
print(list_based_on_string)

# Create a string based on a list of words

string_based_on_list = "".join(
    list_based_on_string
)  # will put the initial string between the elements, so we can leave it as a space if needed
print(string_based_on_list)
string_based_on_list = " ".join(list_based_on_string)
print(string_based_on_list)


# Create a list based on a string
list_based_on_string = ["a"] * 10
print(list_based_on_string)

# Bad practice: Create a string based on a loop (its MUCH faster and efficient to use .join instead of this)
my_string = ""
for item in list_based_on_string:
    my_string += item

print(my_string)

# Concatenate string and string variables, "%s for strings, %d for integer, %f for floating (decimals), this %f will have 6 digits by default"
some_var = "Tom"
my_string = "the variable is %s" % some_var
print(my_string)

# Another way to do it is with .format
my_string = "the variable is {}".format(some_var)
print(my_string)

# Fast way to concatenate string and variables, use "f" to format, before the string
my_string = f"the variable is {some_var} and {some_var}"
print(my_string)
