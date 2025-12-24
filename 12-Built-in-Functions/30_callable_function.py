# Callable Function

def func():
    pass

class MyClass:
    pass

print(f"Function callable: {callable(func)}")
print(f"Class callable: {callable(MyClass)}")
print(f"String callable: {callable('hello')}")