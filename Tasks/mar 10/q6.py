"""
6. Create a class Person with a constructor that initializes name and city. Display the information.

"""

class Person:

    def __init__(self,name,city):
        self.name = name
        self.city = city
        
    def display(self):

        print(self.name,self.city)


person_instance = Person("edwin","Thrissur")

person_instance.display()