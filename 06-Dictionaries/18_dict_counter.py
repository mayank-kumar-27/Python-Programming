# Dict Counter

from collections import Counter
items = input("Enter items separated by space: ").split()
counter = Counter(items)
print("Counter:", counter)