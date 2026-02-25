"""
16. Write a program to safely access a key from a dictionary without causing an error if the key does not exist.

"""

stu_details = {"edwin":76,"sreerag": 46,"gopi":39,"rahul":77}

print(stu_details.get("edwin","Key doesn't exist"))