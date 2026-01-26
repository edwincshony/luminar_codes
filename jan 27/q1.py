"""
Write a Python program using match–case to display the day of the week based on a number (1–7).
"""

day = int(input("Enter day of the week (1–7): "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number")
