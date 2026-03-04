fr = open("12.file_operations\\food_logs\\food_log.txt")

foods_logs = []

for line in fr:

    data = line.rstrip("\n").split(",")

    log = {"id":int(data[0]),"meal_type":data[1],"name":data[2],"calorie":float(data[3]),"date":data[4],"owner":data[5]}

    foods_logs.append(log)

print(foods_logs)

# food with high calory

high_calory = max(c.get("calorie") for c in foods_logs)

food_with_high_cal = [c.get("name") for c in foods_logs if c.get("calorie") == high_calory]

print(food_with_high_cal)

# all cuisines

all_cusines = {c.get("meal_type") for c in foods_logs}
print(all_cusines)

# 