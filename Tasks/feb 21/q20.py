"""
20. Convert a dictionary into a list of tuples.

"""

stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":77}

tup_list = []

for keys,values in stu_details.items():

    tup_list.append((keys,values))

print(tup_list)
