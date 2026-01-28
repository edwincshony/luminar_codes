"""
5. Exam Result System
------------------------------------
Task:
- Ask for roll number

If roll number exists:
    - Ask for marks
    - If marks ≥ 40:
        "Pass"
    - Else:
        "Fail"
Else:
    "Invalid roll number"
"""

db_roll_nos = [10,11,12] 

roll_no = int(input("enter roll no: "))

if roll_no in db_roll_nos:
    marks = int(input("enter marks: "))
    if marks >= 40:
        print("pass")
    else:
        print("fail")
else:
    print("Invalid roll number")