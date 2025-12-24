# Tuple Sorting

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
my_tuple = tuple(numbers)
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:", sorted_tuple)