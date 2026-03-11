class Brand:

    def __init__(self,name):
        self.name = name

    def display(self):

        print(self.name)

class Product(Brand):

    def __init__(self,name,title,price):
        super().__init__(name)
        self.title = title
        self.price = price

    def display(self):

        super().display()

        print(self.title,self.price)

product_instance = Product("Cadbury","Dairy Milk",200)

product_instance.display()
    