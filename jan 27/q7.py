"""
Write a program using match–case to check whether a given number is positive, negative, or zero.
"""

number = int(input("enter number: "))

match number:
    case number if number > 0:
        print(number, "is positive")
    case number if number < 0:
        print(number, "is negative")
    case 0:
        print("zero")
