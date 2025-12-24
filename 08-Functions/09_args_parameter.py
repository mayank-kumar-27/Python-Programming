# Args Parameter

def print_args(*args):
    for arg in args:
        print(arg)

items = input("Enter items separated by space: ").split()
print_args(*items)