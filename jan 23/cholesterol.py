"""
4) Cholesterol Level Check

Input: cholesterol
Conditions:

If cholesterol < 200 → Desirable

If cholesterol between 200 and 239 → Borderline High

If cholesterol ≥ 240 → High Cholesterol
"""

cholesterol = int(input("enter cholesterol value: "))

if cholesterol < 200:
    print("Desirable")
elif cholesterol <=239:
    print("Borderline High")
else:
    print("High Cholesterol")
