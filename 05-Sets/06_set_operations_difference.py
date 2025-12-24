# Set Operations Difference

set1 = set(input("Enter first set items separated by space: ").split())
set2 = set(input("Enter second set items separated by space: ").split())
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)