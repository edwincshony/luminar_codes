"""
4. Create a class Car with a constructor that initializes brand and model. Print the car details using a method.

"""

class Car:

    def __init__(self,brand,model):
        
        self.brand = brand
        self.model = model

    def display(self):

        print(self.brand,self.model)

car_instance = Car("maruthi suzuki","wagon r")

car_instance.display()

