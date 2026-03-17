"""10. Write a program to check the memory address of original list and copied list using id().
"""

# original list
favs = ["polo", "creta", "tiago"]

# copied list (shallow copy)
favs_copy = favs.copy()

# print memory addresses
print("Original ID:", id(favs))
print("Copy ID:", id(favs_copy))
print("Is both ids same",id(favs) == id(favs_copy))