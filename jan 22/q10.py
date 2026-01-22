"""
🔟 Write a Python program to check username and password and display login success or failure.
"""

username = input("enter username")

password = input("enter password")

if username == "admin" and password == "password":
    print("login success")
else:
    print("login failure")


