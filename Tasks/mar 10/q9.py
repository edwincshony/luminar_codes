""""
9. Create a class Laptop with a constructor that initializes brand and RAM size. Print the laptop specifications.

"""

class Laptop:

    def __init__(self,brand,ram_size):
        self.brand = brand
        self.ram_size = ram_size

    def display(self):

        print(self.brand,self.ram_size)

laptop_inst = Laptop("Lenovo",8)

laptop_inst.display()