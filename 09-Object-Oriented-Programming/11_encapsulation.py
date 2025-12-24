# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

balance = float(input("Enter balance: "))
account = BankAccount(balance)
print("Balance:", account.get_balance())