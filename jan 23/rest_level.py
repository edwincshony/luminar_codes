"""
9) Resting Energy Level

Input: energy_score (1–10)
Conditions:

If score between 1 and 3 → Low Energy

If score between 4 and 7 → Moderate Energy

If score between 8 and 10 → High Energy
"""
energy_score = int(input("enter value: "))

if energy_score >= 1 and energy_score <= 3:
    print("Low Energy")
elif energy_score >= 4 and energy_score <= 7:
    print("Moderate Energy")
elif energy_score >= 8 and energy_score <= 10:
    print("High Energy")
else:
    print("invalid")