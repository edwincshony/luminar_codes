"""
11. Create a dictionary of student names and marks. Print students who scored above 75.

"""

stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":77}

for key,value in stu_details.items():

    if value > 75:

        print(key)