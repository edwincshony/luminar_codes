"""
8. Write a program to check whether a given number is a palindrome using a while loop.

"""

"""
“If I need digit 1 → use != 0
If 1 does nothing → use > 1”
"""

number = int(input("enter number: "))

org_number = number

reverse = 0

while(number!=0):

    ld = number % 10

    reverse = reverse * 10 + ld

    number = number // 10

if reverse == org_number:

    print("palindrome")

else:

    print("not palindrome")