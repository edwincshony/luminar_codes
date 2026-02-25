food_logs = [
    [1, "adithya", "dosa", "meals", "chapathy", 1800],
    [2, "sreya", "dosa", "biriyani", "mandhi", 2000],
    [3, "amritha", "dosa", "mandhi", "porotta", 2000],
    [4, "dijo", "dosa", "mandhi", "meals", 300],
]

# extract lunch column (index 3)
lunch_items  = [lst[3] for lst in food_logs]

print(lunch_items )

# count frequency
lunch_counts  =  {f:lunch_items.count(f) for f in lunch_items}

print(lunch_counts)

# find most liked lunch
most_liked_lunch  = max(lunch_counts,key=lunch_counts.get)

print(most_liked_lunch)