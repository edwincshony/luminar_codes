"""
19. Write a program to check temperature status.
* Below 20 → Cold
* 20–30 → Normal
* Above 30 → Hot
"""

temperature_status = int(input("enter temperature status: "))

if temperature_status < 20:
    print("cold")
elif temperature_status <= 30:
    print("Normal")
else:
    print("Hot")