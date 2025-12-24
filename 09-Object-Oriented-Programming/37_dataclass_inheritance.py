# Dataclass Inheritance

from dataclasses import dataclass

@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

name = input("Enter dog name: ")
breed = input("Enter breed: ")
d = Dog(name, breed)
print(d)