"""
2.  Body Mass Index (BMI) Category

Input: bmi
Conditions:

If bmi < 18.5 → Underweight

If bmi between 18.5 and 24.9 → Normal Weight

If bmi between 25 and 29.9 → Overweight

If bmi ≥ 30 → Obese
"""

bmi = float(input("enter bmi value: "))

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal Weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
