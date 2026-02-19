daily_calories = {

    "sunday" : 18000,
    "monday" : 18000,
    "tue": 1500,
    "wed": 2900,
    "thurs": 15000,
    "fri": 19000,
            "sat": 2148
}

# for key in daily_calories:

#     print(key,daily_calories[key])


total_calories = 0

for key in daily_calories:

    cal = daily_calories[key]

    total_calories += cal

print(total_calories)

print(total_calories/len(daily_calories))

