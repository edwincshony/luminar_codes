"""
9. Write a Python program to print each digit of a number separately using a while loop.

"""

number = int(input("enter number: "))

while(number!=0):

    last_digit = number % 10

    print(last_digit)

    number = number // 10