# Class it is a description of object\instance
# Instance\object it is variable with Class type
# function inside class is method
# variable in class it is a class variable or class field
# each class contain <constructor> or init method what call when we will create an instance of class

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"Car: {self.model} in {self.color}"

    def drive(self):
        print("Brbrbrbrbrbr bip bip bip........")


class Truck(Car):

    def __init__(self, model, color, wheels_quantity, type):
        Car.__init__(self, model, color)
        self.wheels_quantity = wheels_quantity
        self.type = type

    def __str__(self):
        return f"Truck with type: {self.type} with model: {self.model} in color: {self.color} with wheels: {self.wheels_quantity}"


bmw5 = Car("BMW M5", "BLACK")
print(bmw5)

kamaz = Truck("Kamaz", "Red", 10, "big_truck")
print(kamaz)
