"""
1. Write a program to swap two tuples.

"""

tup1 = (1,2,3,4,5)
tup2=(6,7,8,9,10)
temp = ()

print("Before swapping ----------")

print(f"tuple 1 = {tup1}")
print(f"tuple 2 = {tup2}")

temp = tup1
tup1 = tup2
tup2 = temp

print("After swapping ----------")

print(f"tuple 1 = {tup1}")
print(f"tuple 2 = {tup2}")
