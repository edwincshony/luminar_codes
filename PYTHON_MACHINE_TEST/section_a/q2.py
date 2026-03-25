"""2. Write a program to reverse a number (without converting to string).
"""

number = int(input("enter the number to reverse: "))

rev = 0

while number!=0:

    ld = number % 10

    rev = rev * 10 + ld

    number //= 10

print(rev)