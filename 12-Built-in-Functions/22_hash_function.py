# Hash Function

value = input("Enter a value: ")
try:
    print(f"Hash: {hash(value)}")
except TypeError:
    print("Value is not hashable")