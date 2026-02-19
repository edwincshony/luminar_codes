"""
7) Screen Time Health Check

Input: screen_hours
Conditions:

If screen_hours < 2 → Healthy Usage

If screen_hours between 2 and 5 → Moderate Usage

If screen_hours > 5 → Excessive Usage
"""

screen_hours = int(input("enter screen hours: "))

if screen_hours < 2:
    print("Healthy Usage")
elif screen_hours <= 5:
    print("Moderate Usage")
else:
    print("Excessive Usage")