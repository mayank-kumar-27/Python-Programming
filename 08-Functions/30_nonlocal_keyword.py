# Nonlocal Keyword

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print("Nonlocal x:", x)

outer()