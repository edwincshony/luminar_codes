# most_liked_meal find from all food

food_logs = [
    [1, "adithya", "dosa", "meals", "chapathy", 1800],
    [2, "sreya", "dosa", "biriyani", "mandhi", 2000],
    [3, "amritha", "dosa", "mandhi", "porotta", 2000],
    [4, "dijo", "dosa", "mandhi", "meals", 300],
]

all_foods = []

for log in food_logs:

    all_foods.extend(log[2:5])

food_counts = {food: all_foods.count(food) for food in all_foods}

print(food_counts)

# max(food_name, by = how_many_times_eaten)

# max_eat = max(all_fod) # Python checks keys alphabetically, not values.

most_liked_food  = max(food_counts, key=food_counts.get)

print("Most favorite food: ",most_liked_food)