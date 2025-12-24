# Issubclass Function

class Animal:
    pass

class Dog(Animal):
    pass

print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
print(f"Animal is subclass of Dog: {issubclass(Animal, Dog)}")