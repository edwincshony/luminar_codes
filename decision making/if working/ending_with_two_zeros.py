"""
century year 1800
"""

year = int(input("enter number")) # year = 1800

if year % 100 == 0:  # taking last 2 digit ie here 00 ; compare 00 == 0 its correct
    print("century year")
else:
    print("no")