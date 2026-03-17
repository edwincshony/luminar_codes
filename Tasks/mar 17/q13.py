"""13. Create a program that demonstrates shallow copy using the assignment operator (=) and explain the output.
"""

# original list
favs = ["polo", "creta", "tiago"]

# assignment (NOT a real copy)
favs_copy = favs

# modify copied list
favs_copy[0] = "wagon r"

print("Original:", favs)
print("Copy:", favs_copy)