"""14. Write a program where a nested dictionary is copied using deepcopy() and modified without affecting the original dictionary.
"""

from copy import deepcopy

# original nested dictionary
student = {
    "name": "edwin",
    "details": {
        "age": 20,
        "fav_cars": ["polo", "creta"]
    }
}

# deep copy
student_copy = deepcopy(student)

# modify copied dictionary
student_copy["details"]["fav_cars"][0] = "wagon r"

# print both
print("Original:", student)
print("Copy:", student_copy)