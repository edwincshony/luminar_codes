"""9. Create a list of lists and perform shallow copy using slicing. Modify an element and observe the effect.
"""

# original list of lists
favs = [
    ["edwin", "polo"],
    ["dijo", "wagon r"],
    ["sreerag", "baleno"]
]

# shallow copy using slicing
favs_copy = favs[:]

# modify inner element
favs_copy[0][1] = "swift"

print("Original:", favs)
print("Copy:", favs_copy)