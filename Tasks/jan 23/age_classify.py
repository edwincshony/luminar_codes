"""
3.  Age Group Classification

Input: age
Conditions:

If age < 13 → Child

If age between 13 and 19 → Teenager

If age between 20 and 59 → Adult

If age ≥ 60 → Senior Citizen
"""

age = int(input("enter age: "))

if age < 13:
    print("child")
elif age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
