"""
7. Create a class Product with a constructor that initializes product name and price. Print the product details.

"""

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):

        print(self.name,self.price)

pro_inst = Product("LOQ",55000)

pro_inst.display()