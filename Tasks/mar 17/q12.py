"""12. Write a Python program to perform deep copy on a class object and verify that changes in copied object do not affect the original object.
"""

import copy

# define class
class Student:
    def __init__(self, name, fav_cars):
        self.name = name
        self.fav_cars = fav_cars   # nested mutable data

# create original object
s1 = Student("edwin", ["polo", "creta"])

# deep copy
s2 = copy.deepcopy(s1)

# modify copied object
s2.fav_cars[0] = "wagon r"

# print results
print("Original:", s1.name, s1.fav_cars)
print("Copy:", s2.name, s2.fav_cars)