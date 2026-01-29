"""
10. Write a program to find the sum of digits of a given number using a while loop.
"""

number = int(input("enter number: "))

sum = 0

while(number!=0):

    last_digits = number % 10

    sum = sum + last_digits

    number = number // 10

print(sum)
