# Reduce Function

from functools import reduce
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)