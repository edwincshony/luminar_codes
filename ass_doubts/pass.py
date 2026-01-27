"""
15. Write a program to check whether a given password is valid or invalid(Minimum length: 8 characters).

"""

user_password = input("enter password: ")

if len(user_password) < 8:
    print("invalid")
else:
    print("valid")