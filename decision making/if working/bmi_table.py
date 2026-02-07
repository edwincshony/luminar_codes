"""
BMI = weight_in_kg / (height_in_m^2)

display underweight if bmi < 20
display normal if bmi in range of 20 to 25
display overweight if bmi in range of 25 to 30
display obese for rest
"""

weight_in_kg = int(input("enter weight in kg: "))

height_in_cm = int(input("enter height in cm: "))

height_in_m = height_in_cm / 100

bmi = weight_in_kg // (height_in_m ** 2)

bmi = round(bmi)

print("Your bmi is:,",bmi)

if bmi < 20:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("obese")




