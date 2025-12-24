# Tuple Operations

tuple1 = tuple(input("Enter first tuple items separated by space: ").split())
tuple2 = tuple(input("Enter second tuple items separated by space: ").split())
concatenated = tuple1 + tuple2
print("Concatenated:", concatenated)
n = int(input("Enter repetition factor: "))
repeated = tuple1 * n
print("Repeated:", repeated)