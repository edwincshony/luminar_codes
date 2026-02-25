"""
18. Remove multiple keys from a dictionary at once.

"""

stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":77}

keys_to_remove = {"edwin","sreerag"}

for k in keys_to_remove:

    del stu_details[k]

print(stu_details)

