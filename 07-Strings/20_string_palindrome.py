# String Palindrome

my_string = input("Enter a string: ").lower().replace(" ", "")
reversed_str = my_string[::-1]
is_palindrome = my_string == reversed_str
print("Is palindrome:", is_palindrome)