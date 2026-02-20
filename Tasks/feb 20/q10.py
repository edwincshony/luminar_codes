"""

10. Write a program to check whether a given value exists in a set or not.
"""

st = {10,20,30,40,50}

number = int(input("enter the value to check: "))

if number in st:

    print("exists")

else:

    print("doesnt exist")