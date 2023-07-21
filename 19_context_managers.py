# Context Managers: Great tool for resource management, that allow to allocate and release resources when we want to

# Open a file and write something to it using context manager, it also makes sure to free our resources once the write operation is completed
with open("notes.txt", "w") as file:
    file.write("some todo...")


# Manual way without context manager, less efficient
file = open("notes.txt", "w")

try:
    file.write("some todoo....")
finally:
    file.close()
