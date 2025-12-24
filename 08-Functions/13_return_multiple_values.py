# Return Multiple Values

def get_min_max(numbers):
    return min(numbers), max(numbers)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
min_val, max_val = get_min_max(numbers)
print("Min:", min_val, "Max:", max_val)