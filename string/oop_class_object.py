class Person():
    # Defines a class named Person.
    # This is a blueprint for creating Person objects.

    def eat(self):
        # Defines an instance method named eat.
        # 'self' refers to the object that calls this method.

        print("Person is eating")
        # Prints a message when the eat method is called.

    def sleep(self):
        # Defines an instance method named sleep.
        # 'self' again refers to the calling object.

       print("Person is sleeping")
       # Prints a message when the sleep method is called.


edwin_instance = Person()
# variable_name = ClassName()
# Creates an object (instance) of the Person class.
# The variable edwin_instance now refers to this object in memory.

edwin_instance.eat()
# Calls the eat method on the edwin_instance object.
# Python passes edwin_instance to the method as 'self' automatically.

edwin_instance.sleep()
# Calls the sleep method on the edwin_instance object.
# Again, 'self' refers to edwin_instance.
