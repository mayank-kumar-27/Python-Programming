# Scope Local Global

x = 10  # global

def func():
    x = 5  # local
    print("Local x:", x)

func()
print("Global x:", x)