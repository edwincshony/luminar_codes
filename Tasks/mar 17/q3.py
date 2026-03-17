"""3. Create a list containing nested lists. Perform a shallow copy and modify the inner list. Print both lists and observe the result.
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