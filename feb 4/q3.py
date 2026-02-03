"""
3. Write a program to print the grade based on marks:
* 90 and above → A
* 75–89 → B
* 50–74 → C
* Below 50 → Fail
"""

marks = int(input("enter marks: "))

if marks >= 90:

    print("A")

elif marks <= 89 and marks >= 75:

    print("B")

elif marks >= 50 and marks <= 74:

    print("C")

else:

    print("Fail")