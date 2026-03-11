"""
constructor
special name python ( __init__ ), java (classname), javascript (constructor)
automatically invoked during object creation
initialize attributes of an instance
"""

class Mobile():

    def __init__(self,image,name,price,rating):

        self.image = image
        self.name = name
        self.price = price
        self.rating = rating

    def display(self):

        print(self.image,self.name,self.price,self.rating)

mobile_instance = Mobile("samsung galaxy s26.jpg","samsung s26",200000,5) # init is called at time of object creation, then just pass arguments in ()

mobile_instance.display()

