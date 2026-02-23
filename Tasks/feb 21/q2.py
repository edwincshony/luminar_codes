"""
Create a tuple of numbers and find the maximum and minimum values without converting it into a list.
"""

tup = (70, 20, 30, 40, 50)

largest = float('-inf')
smallest = float('inf')

for num in tup:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Minimum is: {smallest}")
print(f"Maximum is: {largest}")






