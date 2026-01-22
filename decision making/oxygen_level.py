"""
4)Oxygen Level (SpO2)
    Input: oxygen_level
    Conditions:
    If oxygen_level >= 95 → Normal
    If oxygen_level between 90 and 94 → Mild Concern
    If oxygen_level < 90 → Critical
"""
oxygen_level = int(input("enter level: "))

if oxygen_level >= 95:
    print("normal")
elif oxygen_level >= 90:
    print("Mild Concern")
elif oxygen_level < 90:
    print("Critical")
