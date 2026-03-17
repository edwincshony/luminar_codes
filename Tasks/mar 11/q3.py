"""3. Create a class Bird with a method fly(). Create subclasses Sparrow and Ostrich that override the fly() method with different behaviors.
"""

class Bird:

    def fly(self):

        print("bird fly method")

class Sparrow(Bird):

    def fly(self):

        print("Sparrow fly method")

class Ostrich(Bird):

    def fly(self):

        print("Ostrich fly method")

sparrow_inst = Sparrow()
sparrow_inst.fly()
ostrich_inst = Ostrich()
ostrich_inst.fly()