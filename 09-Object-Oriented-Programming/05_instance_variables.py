# Instance Variables

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

name = input("Enter dog name: ")
breed = input("Enter breed: ")
dog = Dog(name, breed)
print(f"Name: {dog.name}, Breed: {dog.breed}")