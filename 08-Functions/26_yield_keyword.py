# Yield Keyword

def squares(n):
    for i in range(1, n+1):
        yield i**2

n = int(input("Enter n: "))
for sq in squares(n):
    print(sq)