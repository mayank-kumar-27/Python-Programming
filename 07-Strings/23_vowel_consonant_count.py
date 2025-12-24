# Vowel Consonant Count

my_string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in my_string if char in vowels)
consonant_count = sum(1 for char in my_string if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)