"""10. Create a class Vehicle with a method move(). Create subclasses Car and Airplane that override the move() method.
"""

# base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# subclass 1
class Car(Vehicle):
    def move(self):
        print("Car moves on roads")

# subclass 2
class Airplane(Vehicle):
    def move(self):
        print("Airplane flies in the sky")

# create objects
v1 = Car()
v2 = Airplane()

# call methods
v1.move()
v2.move()