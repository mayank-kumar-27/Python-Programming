# Set Methods Issubset Issuperset

set1 = set(input("Enter first set items separated by space: ").split())
set2 = set(input("Enter second set items separated by space: ").split())
print("set1 is subset of set2:", set1.issubset(set2))
print("set1 is superset of set2:", set1.issuperset(set2))