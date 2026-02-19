"""
8. Write a program using match–case to display the day name when the user enters a number (1–7).

"""
day = int(input("enter day number: "))
match day:
    case 1: print("sun")
    case 2: print("Monday")
    case 3: print("Tue")
    case 4: print("wed")
    case 5: print("thurs")
    case 6: print("fri")
    case 7: print("sat")
    case _: print("invalid")