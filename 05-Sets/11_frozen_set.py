# Frozen Set

my_set = set(input("Enter items separated by space: ").split())
frozen = frozenset(my_set)
print("Frozen set:", frozen)
print("Type:", type(frozen))