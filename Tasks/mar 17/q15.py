"""15. Write a Python program to demonstrate the difference between shallow copy and deep copy with a practical example.
"""

import copy

# original data (nested list)
favs = [
    ["edwin", ["polo", "creta"]],
    ["dijo", ["wagon r", "swift"]]
]

# shallow copy
shallow_copy = copy.copy(favs)

# deep copy
deep_copy = copy.deepcopy(favs)

# modify nested element
shallow_copy[0][1][0] = "baleno"
deep_copy[1][1][0] = "i20"

# print all
print("Original:", favs)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)