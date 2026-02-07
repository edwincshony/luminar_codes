"""
read a number
chk num is / by 8
    yes display number is divisible by 8
    no display number is not divisible by 8
"""

number = int(input("Enter number: "))

if number % 8 == 0:
    print("yes display number is divisible by 8")
else:
    print("no display number is not divisible by 8")