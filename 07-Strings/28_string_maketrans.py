# String Maketrans

from_str = input("Enter characters to replace: ")
to_str = input("Enter replacement characters: ")
trans_table = str.maketrans(from_str, to_str)
my_string = input("Enter string to translate: ")
translated = my_string.translate(trans_table)
print("Translated:", translated)