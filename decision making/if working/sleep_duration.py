"""
5)Sleep Duration Health Check
    Input: hours_of_sleep
    Conditions:
    If sleep < 6 → Sleep Deprived
    If sleep between 6 and 8 → Healthy Sleep
    If sleep > 8 → Oversleeping
"""

hours_of_sleep = int(input("enter your hours of sleep: "))

if hours_of_sleep < 6:
    print("Sleep Deprived")
elif hours_of_sleep >= 6 and hours_of_sleep <=8:
    print("Healthy Sleep")
elif hours_of_sleep > 8:
    print("Oversleeping")