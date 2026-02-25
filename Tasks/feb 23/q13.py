"""
13. Given a dictionary, print the key with the highest value.

"""
stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":81}

max_value = float('-inf')

max_key = None

for key,value in stu_details.items():

    if value > max_value:

        max_value = value

        max_key = key

print(max_key)



