# Class Object Creation

class Car:
    def __init__(self, model):
        self.model = model

model = input("Enter car model: ")
car = Car(model)
print("Car model:", car.model)