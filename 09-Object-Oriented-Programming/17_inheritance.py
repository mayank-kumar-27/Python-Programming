# Inheritance

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print("Dog speaks:", dog.speak())