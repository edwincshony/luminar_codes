"""7. Create a dictionary containing a list as a value. Perform shallow copy and modify the list. Print both dictionaries.
"""

# original dictionary
student = {
    "name": "edwin",
    "fav_cars": ["polo", "creta", "tiago"]
}

# shallow copy
student_copy = student.copy()

# modify the list inside the copy
student_copy["fav_cars"][0] = "wagon r"

print("Original:", student)
print("Copy:", student_copy)