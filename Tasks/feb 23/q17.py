"""
17. Merge two dictionaries. If duplicate keys exist, keep the higher value.

"""

stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":77}
employee_details = {"edwin":74,"akshay": 56,"alen":19,"manoj":67}

for key in stu_details:

    if stu_details[key] == employee_details[key]:

        print