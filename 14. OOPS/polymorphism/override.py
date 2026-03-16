"""
2) METHOD OVERRIDING = child class redifines the method that is defined in parent class
"""
class Parent:

    def bike(self):

        print("passion pro")

    def car(self):

        print("swift")

class Child(Parent):

    def bike(self):

        print("bullet")

    def car(self):

        print("polo gt")

child_inst = Child()

child_inst.bike()
child_inst.car()
