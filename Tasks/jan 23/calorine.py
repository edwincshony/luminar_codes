"""
10) Daily Calorie Intake

Input: calories
Conditions:

If calories < 1500 → Low Intake

If calories between 1500 and 2500 → Balanced Intake

If calories > 2500 → Excess Intake
"""

calories = int(input("enter daily calorie intake: "))

if calories < 1500:
    print("Low Intake")
elif calories <= 2500:
    print("Balanced Intake")
else:
    print("Excess Intake")
