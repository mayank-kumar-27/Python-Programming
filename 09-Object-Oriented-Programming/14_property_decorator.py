# Property Decorator

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

c = Celsius(25)
print("Temperature:", c.temperature)