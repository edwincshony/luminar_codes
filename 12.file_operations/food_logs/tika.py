fr = open("12.file_operations\\food_logs\\food_log.txt")
food_log=[]
for line in fr:

    data = line.strip().split(",")

    log = {"id":data[0],"meal_type":data[1],"name":data[2],"calorie":data[3],"date":data[4],"owner":data[5]}

    food_log.append(log)

print(food_log)