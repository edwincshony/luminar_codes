"""
18. Write a program to display day type based on day number.
* 1–5 → Working day
* 6–7 → Weekend
"""

day_number = int(input("enter day number: "))

if day_number >= 1 and day_number <= 5:
    print("Working day")
elif day_number >= 6 and day_number <= 7 :
    print("Weekend")
else:
    print("enter number from 1 - 7")
