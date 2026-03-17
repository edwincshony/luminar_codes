"""7. Create a class Shape with a method draw(). Create subclasses Square and Triangle that override the draw() method.
"""

class Shape:

    def draw(self):

        print("shape method")

class Square(Shape):

    def draw(self):

        print("square method")

class Triangle(Shape):

    def draw(self):

        print("triangle method")

dev_inst = Square()
dev_inst.draw()
man_inst = Triangle()
man_inst.draw()