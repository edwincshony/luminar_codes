"""
read fasting_blood_sugar
normal < 100
prediabets 100 - 125
diabets > 125
"""

fasting_blood_sugar = int(input("Enter value: "))
if fasting_blood_sugar < 100:
    print("normal")
elif fasting_blood_sugar <= 125:
    print("prediabets")
elif fasting_blood_sugar > 125:
    print("diabets")