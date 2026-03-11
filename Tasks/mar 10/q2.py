"""
2. Create a class Rectangle with a constructor that takes length and width. Write a method to calculate the area of the rectangle.

"""

class Rectangle:

    def __init__(self,length,width):

        self.length = length
        self.width = width
        self.area = 0

    def cal_area(self):

        self.area = self.length * self.width
        print(self.area)

rect_instance = Rectangle(12,10)

rect_instance.cal_area()
        
      
