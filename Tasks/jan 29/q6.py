"""
6. Write a program to count the number of digits in a given number using a while loop.

"""

"""
“If I need digit 1 → use != 0
If 1 does nothing → use > 1”
"""

number = int(input("enter number: "))

org_number = number

count = 0

if number == 0:

    count = 1

else:

    while(number != 0):

        number = number // 10

        count = count + 1

print(f"The number of digits in number {org_number} is {count}")
