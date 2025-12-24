# Method Types Comparison

class Example:
    class_var = "class"

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def instance_method(self):
        return self.instance_var

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "static"

ex = Example("instance")
print("Instance:", ex.instance_method())
print("Class:", Example.class_method())
print("Static:", Example.static_method())