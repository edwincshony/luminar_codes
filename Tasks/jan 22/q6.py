"""
6️⃣ Write a Python program to display the grade of a student using the following rules:

Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail
"""

Marks = int(input("enter marks"))

if Marks >= 90:
    print("Grade A")
elif Marks >= 75:
    print("Grade B")
elif Marks >= 50:
    print("Grade C")
else:
    print("Fail")