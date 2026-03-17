"""11. Create a class object and perform shallow copy of the object using the copy module.
"""

import copy

# define a class
class Student:
    def __init__(self, name, fav_cars):
        self.name = name
        self.fav_cars = fav_cars   # nested (mutable)

# create object
s1 = Student("edwin", ["polo", "creta"])

# shallow copy
s2 = copy.copy(s1)

# modify nested data
s2.fav_cars[0] = "wagon r"

# print results
print("Original:", s1.name, s1.fav_cars)
print("Copy:", s2.name, s2.fav_cars)