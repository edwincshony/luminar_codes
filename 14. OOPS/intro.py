"""
Key OOP Concepts Demonstrated
-----------------------------

1. Class
A class is a blueprint used to create objects.

Examples:
    class Animal
    class Student


2. Object
An object is an instance of a class.

Examples:
    cat_instance = Animal()
    edwin_instance = Student()


3. Method
A method is a function defined inside a class.

Examples:
    walk()
    jump()
    set_student()
    display()


4. self Keyword
The 'self' keyword refers to the current instance of the class.

Example:
    self.name = name

Meaning:
    edwin_instance.name = "edwin"

Here, 'self.name' refers to the 'name' attribute of the specific object
that calls the method.
"""


class Animal:

    # attributes

    color: str
    size: str
    sound: str

    #functionalities/methods

    def walk(self):

        print("Animal walk method")

    def jump(self):

        print("Animal jump method")

cat_instance = Animal() # Creates an object (instance) of the Animal class.

dog_instance = Animal() # Creates an object (instance) of the Animal class.

cat_instance.walk() #cat_instance comes to self in walk, self is a keyword which is used to point current instance
cat_instance.walk() #

dog_instance.walk()