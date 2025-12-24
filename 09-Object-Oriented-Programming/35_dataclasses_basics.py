# Dataclasses Basics

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

name = input("Enter name: ")
age = int(input("Enter age: "))
p = Person(name, age)
print(p)