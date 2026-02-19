"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists

"""

stu_details = {"id":"221021","name":"edwin","course":"data science","marks":70}

print(stu_details["name"])

stu_details["marks"] = stu_details["marks"] + 5

stu_details["grade"] = "A"

if "attendence" in stu_details:

    print("yes")

else:

    print("no")

print(stu_details)

