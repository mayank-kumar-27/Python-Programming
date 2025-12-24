# Name Mangling

class Test:
    def __init__(self):
        self.__private = "private"

t = Test()
print("Mangled name:", hasattr(t, '_Test__private'))