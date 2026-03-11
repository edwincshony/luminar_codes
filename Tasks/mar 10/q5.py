"""
5. Create a class Circle with a constructor that takes radius. Write a method to calculate the area of the circle.

"""

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def cal_area(self):

        const = 3.14

        self.area = const * self.radius ** 2

        print(self.area)

circle_instance = Circle(2)

circle_instance.cal_area()