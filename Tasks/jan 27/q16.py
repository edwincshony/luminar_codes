"""
16. Write a program to determine the type of number based on its value.
* Less than 0 → Negative
* Equal to 0 → Zero
* Greater than 0 → Positive
"""

number = int(input("enter number: "))

if number < 0:
    print("Negative")
elif number > 0:
    print("Positive")
else:
    print("Zero")