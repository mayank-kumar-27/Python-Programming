# Set Operations Symmetric Difference

set1 = set(input("Enter first set items separated by space: ").split())
set2 = set(input("Enter second set items separated by space: ").split())
sym_diff = set1.symmetric_difference(set2)
print("Symmetric difference:", sym_diff)