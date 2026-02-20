"""
5. Write a program to find the maximum and minimum value in a tuple.

"""

numbers = (23, 45, 12, 67, 34, 8, 56)

maximum = float('-inf')

minimum = float('inf')

for num in numbers:

    if num > maximum:

        maximum = num
    
    if num < minimum:

        minimum = num

print(minimum)

print(maximum)