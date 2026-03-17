"""1. Write a Python program to create a list and make a shallow copy of it using the copy() method.
"""

evens = [i for i in range(1,11) if i%2 == 0]
evens_copy = evens.copy()
evens_copy[0] = 99
print("Original list:", evens)
print("Shallow copy:", evens_copy)