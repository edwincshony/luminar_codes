"""
bmi in range of 19 to 25
"""

h_in_cm = 173 #height in cm

w_in_kg = 63 #weight in kg

h_in_m = h_in_cm / 100 #height in meter conversion

bmi = w_in_kg/(h_in_m**2) #bmi calculation

is_bmi_in_range = bmi >= 19 and bmi <= 25

print("Your bmi is:",bmi)

print(is_bmi_in_range)