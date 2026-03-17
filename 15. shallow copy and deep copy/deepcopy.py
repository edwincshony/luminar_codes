# shallow copy only creates copy of outer object
# deep copy creates copy of inner object and outer object

from copy import deepcopy # Import the deepcopy function from the copy module

arun_fvt_colors = [

    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish meal"},
    {"meal_type":"dinner","meal":"fried rice"},
]

hari_fvt_foods = deepcopy(arun_fvt_colors) 

hari_fvt_foods[0]["meal"] = "idly"

print("arun",arun_fvt_colors)
print("hari",hari_fvt_foods)