# Generator Functions

def countdown(n):
    while n > 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
for num in countdown(n):
    print(num)