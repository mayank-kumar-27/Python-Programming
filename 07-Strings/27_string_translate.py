# String Translate

my_string = input("Enter a string: ")
trans = str.maketrans("aeiou", "12345")
translated = my_string.translate(trans)
print("Translated:", translated)