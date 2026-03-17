# 9. Create a class Animal with a method eat(). Create subclasses Lion and Cow that override the eat() method.

# base class
class Animal:
    def eat(self):
        print("Animals eat food")

# subclass 1
class Lion(Animal):
    def eat(self):
        print("Lion eats meat")

# subclass 2
class Cow(Animal):
    def eat(self):
        print("Cow eats grass")

# create objects
a1 = Lion()
a2 = Cow()

# call methods
a1.eat()
a2.eat()