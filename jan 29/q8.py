"""
8. Write a program to check whether a given number is a palindrome using a while loop.

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