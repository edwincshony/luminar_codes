"""
Write a program using match–case to print the number of days in a month based on the month name.
"""

month_name = input("enter month name: ")

thirty_one_days = ["jan", "mar", "may", "july", "aug", "oct", "dec"]

thirty_days = ["june", "nov", "apr", "sep"]

feb = ["feb"]

match month_name:
    case month_name if month_name in thirty_one_days:
        print("31 days")
    case month_name if month_name in thirty_days:
        print("30 days")
    case month_name if month_name in feb:
        print("28/29 days")
    case _: print("invalid month")
    