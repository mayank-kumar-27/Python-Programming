# Static Methods

class Utils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

n = int(input("Enter n: "))
print("Is even:", Utils.is_even(n))