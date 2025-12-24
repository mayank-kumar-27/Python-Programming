# File Methods

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    print(f"Name: {f.name}")
    print(f"Mode: {f.mode}")
    print(f"Closed: {f.closed}")