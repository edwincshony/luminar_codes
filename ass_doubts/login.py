"""
✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"


"""

db_password = "pass"

db_otp = "1542"

user_password = input("enter user password: ")

if db_password == user_password:
    user_otp = input("enter user otp: ")
    if db_otp == user_otp:
        print("Login successful")
    else:
        print("Incorrect OTP")
else:
    print("Incorrect password")