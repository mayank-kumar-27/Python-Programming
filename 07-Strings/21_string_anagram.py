# String Anagram

str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")
is_anagram = sorted(str1) == sorted(str2)
print("Is anagram:", is_anagram)