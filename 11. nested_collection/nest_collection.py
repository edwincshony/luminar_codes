# ----------------------------
# DATA
# ----------------------------

food_vlogs = [
    [1, "adithya", "dosa", "meals", "chapathy", 1800],
    [2, "sreya", "dosa", "biriyani", "mandi", 2000],
    [3, "amritha", "dosa", "mandhi", "porotta", 2000],
    [4, "dijo", "dosa", "mandhi", "meals", 300],
]

social_media_posts = [
    [1, "good morning", 500, 600, "arun"],
    [2, "elon vs trump", 7000, 9000, "vipin"],
    [3, "epstien files", 14000, 1500, "dijo"],
    [4, "nigal njettum", 15000, 80000, "edwin"],
]

# ----------------------------
# BASIC INDEX ACCESS
# ----------------------------

print(food_vlogs[1][5])   # calories
print("--------------")
print(food_vlogs[3][4])   # 3rd food item

# ----------------------------
# MOST CALORIE FOOD VLOGGER
# ----------------------------

max_cal = max(row[5] for row in food_vlogs)
max_cal_people = [row[1] for row in food_vlogs if row[5] == max_cal]

print("Max calorie people:", max_cal_people)

# ----------------------------
# SOCIAL MEDIA ANALYSIS
# ----------------------------

print("--------------")
print(social_media_posts[2][2])  # Facebook views

# All Facebook views
facebook_views = [row[2] for row in social_media_posts]
print("Facebook views:", facebook_views)

# Max Facebook views
max_fb = max(facebook_views)
print("Max Facebook views:", max_fb)

# All Instagram views
insta_views = [row[3] for row in social_media_posts]
print("Instagram views:", insta_views)

# Post owners
owners = [row[4] for row in social_media_posts]
print("Owners:", owners)

# ----------------------------
# FILTERS
# ----------------------------

# People who ate dosa
dosa_people = [row[1] for row in food_vlogs if row[2] == "dosa"]

# People whose 2nd food is meals
meals_people = [row[1] for row in food_vlogs if row[3] == "meals"]

# Insta views > 1000
insta_view_filter = [row[4] for row in social_media_posts if row[3] > 1000]

print("Dosa people:", dosa_people)
print("Meals people:", meals_people)
print("Insta >1000 owners:", insta_view_filter)