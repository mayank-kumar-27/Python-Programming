# Custom Exceptions

class MyError(Exception):
    pass

try:
    value = input("Enter 'error' to raise exception: ")
    if value == 'error':
        raise MyError("Custom error occurred")
    print("No error")
except MyError as e:
    print(e)