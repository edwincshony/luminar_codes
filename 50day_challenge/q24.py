def average_calories():

    calories = []

    while True:

        calorie_intake = input("Enter the calories or done: ")

        if calorie_intake == "done":

            break

        calories.append(int(calorie_intake))

    return sum(calories)/len(calories)
    
print(average_calories())

