# Built-in Exceptions

# Examples of built-in exceptions
try:
    # IndexError
    lst = [1, 2, 3]
    print(lst[int(input("Enter index: "))])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Invalid index")