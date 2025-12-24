# List Sorting Custom

words = input("Enter words separated by space: ").split()
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)