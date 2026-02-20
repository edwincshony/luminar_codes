"""
2. Write a program to count how many times the value 10 appears in a tuple.

"""

tup = (10,20,10,15,48,10,14,10)

c = 0

for num in tup:

    if num == 10:

        c += 1

print(f"10 appeared {c} times in tuple")