"""6. Write a program to compare shallow copy and deep copy using nested lists.
"""
#shallow copy
edwin_fav_cars =  [["polo","creta"], ["tiago","swift"]]

sreerag_fav_cars = edwin_fav_cars.copy()

sreerag_fav_cars[0][0] = "wagon r"

print(edwin_fav_cars)

print(sreerag_fav_cars)

#deep copy

from copy import deepcopy

favs = [
    ["edwin","loq","passion pro","wagon r","tws"],
    ["dijo","hp","passion","wagon r","tws"],
    ["sreerag","loq","splender","baleno","tws"],
]

favs_copy = deepcopy(favs)
favs_copy[1][3] = "swift"

print(favs)
print(favs_copy)