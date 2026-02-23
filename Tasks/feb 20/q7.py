"""
7. Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, write a program to find:
* Common elements
* All unique elements from both sets

"""

st1 = {1,2,3,4}

st2 = {3,4,5,6}

unique_elements = st1.union(st2)

common_elements = st1.intersection(st2)

print(f"Common elements are: {common_elements}")
print(f"Unique elements are: {unique_elements}")


