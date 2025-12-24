# Polymorphism

class Bird:
    def fly(self):
        return "Bird flies"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies low"

birds = [Bird(), Sparrow()]
for bird in birds:
    print(bird.fly())