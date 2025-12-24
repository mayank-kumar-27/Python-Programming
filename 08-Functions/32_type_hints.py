# Type Hints

from typing import List

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum_list(numbers))