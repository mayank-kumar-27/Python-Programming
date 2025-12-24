# Decorators With Parameters

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()