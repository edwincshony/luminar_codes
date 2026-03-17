"""5. Create a nested list and perform deep copy. Modify the inner list and show that the original list remains unchanged.
"""

data = [

    ["edwin",22,"data science","luminar"],
    ["dijo",21,"django","luminar"],
    ["akshay",18,"data science","luminar"],
    ["alan",21,"data science","luminar"],
]

data_copy = data.copy()

data_copy[0][0] = "ramu"

print("Original list:", data)
print("Shallow copy:", data_copy)