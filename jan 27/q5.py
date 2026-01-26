"""
Write a program using match–case to display the month name based on the month number.
"""

month_number = int(input("enter month number ( 1 - 12 ): "))

match month_number:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case 8: print("August")
    case 9: print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")
    case _: print("invalid month number")