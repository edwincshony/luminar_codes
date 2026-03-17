
"""
2. Create two classes Rectangle and Circle. Both classes should have a method area(). Calculate the area for each shape.

"""

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):

        print("Area of rectangle is:",self.length*self.width)

class Circle:

    def __init__(self,pi,radius):
        self.radius = radius
        self.pi = pi

    def area(self):

        print("Area of circle",self.pi*self.radius**2)

rect_inst = Rectangle(4,5)
rect_inst.area()
circle_inst = Circle(3.14,2)
circle_inst.area()