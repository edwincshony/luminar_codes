"""
1. Body Temperature Status

Input: body_temperature (°C)
Conditions:

If temperature < 36 → Low Body Temperature

If temperature between 36 and 37.5 → Normal

If temperature > 37.5 → Fever
"""
body_temperature = float(input("enter body temperature"))

if body_temperature < 36:
    print("Low Body Temperature")
elif body_temperature >= 36 and body_temperature <= 37.5:
    print("normal")
else:
    print("fever")