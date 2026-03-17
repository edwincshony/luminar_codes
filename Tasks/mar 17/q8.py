"""8. Write a Python program that uses deepcopy() to copy a dictionary with nested data.
"""
from copy import deepcopy
edwin_fav_foods = [
    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"cb"},
    {"meal_type":"dinner","meal":"porotta"},
]

edwin_fav_foods_copy = deepcopy(edwin_fav_foods)

edwin_fav_foods_copy[0]["meal"] = "poori"

print(edwin_fav_foods)
print(edwin_fav_foods_copy)