"""3. Write a program to find the largest element in a list.
"""

largest = float('-inf')

lst = [-1,-100]

for num in lst:

    if num > largest:

        largest = num

print(largest)