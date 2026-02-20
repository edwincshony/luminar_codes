"""
14. Write a program to find the second largest element in a list
    (without sorting).
"""

#elif used to prevent below issues
"""
So when a number is:

less than largest

but greater than second_largest

👉 It is ignored.
"""

# Sample list (you can change this)
numbers = [14, 46, 47, 86, 92, 52, 48, 36, 66, 85]

# Initialize largest and second largest to very small numbers
largest = float('-inf')
second_largest = float('-inf')

# Loop through the list once
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num 

    elif num > second_largest and num != largest:
        second_largest = num

# Print the result (handles lists with at least 2 elements)
print("Second largest:", second_largest)
