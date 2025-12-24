# Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter n: "))
print("Factorial:", factorial(n))