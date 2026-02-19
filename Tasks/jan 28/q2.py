"""
2. Login System
------------------------------------
Task:
- Ask for username
- Ask for password

If username and password are correct:
    "Login successful"
Else:
    "Invalid credentials"
"""

db_username = "edwin"
db_password = "pass"

username = input("enter username: ")
password = input("enter password: ")

if db_username == username and db_password == password:
    print("Login successful")
else:
    print("Invalid credentials")