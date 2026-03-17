"""2. Write a program to demonstrate shallow copy using the copy module.
"""

import copy
evens = [i for i in range(1,11) if i%2 == 0]
evens_copy = copy.copy(evens)
evens_copy[0] = 99
print("Original list:", evens)
print("Shallow copy:", evens_copy)