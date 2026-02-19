"""
2)Write a Python program using if elif else to print the health status.
Blood Pressure Category
    Input: systolic_bp
    Conditions:
    If bp < 120 → Normal
    If bp between 120 and 129 → Elevated
    If bp between 130 and 139 → High BP Stage 1
    If bp >= 140 → High BP Stage 2
"""

systolic_bp = int(input("Enter value: "))

if systolic_bp < 120:
    print("normal")
elif systolic_bp >= 120 and systolic_bp <= 129:
    print("Elevated")
elif systolic_bp >= 130 and systolic_bp <= 139:
    print("High BP Stage 1")
elif systolic_bp >= 140:
    print("High BP Stage 2")
else:
    print("invalid ....")