'''
bmi (body mass index)
bmi = weight_in_kg / (height_in_meter)^2
'''

h_in_cm = 173 #height in cm

w_in_kg = 63 #weight in kg

h_in_m = h_in_cm / 100 #height in meter conversion

bmi = w_in_kg/(h_in_m**2) #bmi calculation

print(bmi) #bmi value