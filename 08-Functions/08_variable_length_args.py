# Variable Length Args

def sum_all(*args):
    return sum(args)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum_all(*numbers))