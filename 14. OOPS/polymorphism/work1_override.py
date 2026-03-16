class Shape:

    def area(self):

        print("area is calculating")

class Square(Shape):

    def __init__(self,side):
       self.side = side

    def area(self):

        print("Area of sqaure is:",self.side ** 2)

class Rectangle(Shape):

    def __init__(self,length,breadth):

        self.length = length
        self.breadth = breadth

    def area(self):

        print("Area of rectangle is:",self.length*self.breadth)
        

square_inst = Square(4)

square_inst.area()

rect_inst = Rectangle(4,5)

rect_inst.area()