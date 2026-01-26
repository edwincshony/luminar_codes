"""
20. Write a program to determine exam result category.
* Marks ≥ 90 → Distinction
* Marks ≥ 60 → First class
* Marks ≥ 40 → Pass
* Below 40 → Fail
"""

marks = int(input("enter marks: "))

if marks >= 90:
    print("Distinction")
elif marks >= 60:
    print("First class")
elif marks >= 40:
    print("Pass")
elif marks < 40:
    print("Fail")
