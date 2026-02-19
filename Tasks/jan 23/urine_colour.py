"""
8) Hydration Status (Urine Color Scale)

Input: urine_color (1–8 scale)
Conditions:

If color between 1 and 3 → Well Hydrated

If color between 4 and 6 → Mild Dehydration

If color between 7 and 8 → Severe Dehydration
"""

urine_color = int(input("enter value: "))

if urine_color >= 1 and urine_color <= 3:
    print("Well Hydrated")
elif urine_color >= 4 and urine_color <= 6:
    print("Mild Dehydration")
elif urine_color >= 7 and urine_color <= 8:
    print("Severe Dehydration")
else:
    print("Invalid urine color value")