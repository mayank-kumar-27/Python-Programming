# Character Frequency

my_string = input("Enter a string: ")
freq = {}
for char in my_string:
    freq[char] = freq.get(char, 0) + 1
print("Frequency:", freq)