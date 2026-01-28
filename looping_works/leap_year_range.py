"""
w.a.p to display all leap years from 1800 to 2026
"""

year = 1800
while(year<=2026):
    
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

        print(year,end=" ")

    year = year + 1