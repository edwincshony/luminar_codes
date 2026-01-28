"""
7. Write a Python program to reverse a number using a while loop.

"""

number = int(input("enter number: "))

reverse = 0

while(number!=0):

    ld = number % 10

    reverse = reverse * 10 + ld

    number = number // 10

print(reverse)