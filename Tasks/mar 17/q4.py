"""4. Write a Python program to perform deep copy using the deepcopy() function from the copy module.
"""

from copy import deepcopy

arun_fvt_foods = [

    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish meal"},
    {"meal_type":"dinner","meal":"fried rice"},
]

edwin_fav_foods = deepcopy(arun_fvt_foods)

edwin_fav_foods[0]["meal_type"] = "brunch"

print(arun_fvt_foods)
print(edwin_fav_foods)