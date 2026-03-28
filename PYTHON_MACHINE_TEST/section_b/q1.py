"""11. Write a program to find the second largest number in a list.
"""

numbers = [1,2,89,100,500,4]

largest = float('-inf')
s_largest = float('-inf')

for num in numbers:

    if num > largest:

        s_largest = largest
        largest = num

    elif num > s_largest and num != largest:

        s_largest = num

print("Second largest:",s_largest)
print("largest:",largest)