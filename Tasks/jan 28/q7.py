"""
7. Mobile Unlock System
------------------------------------
Task:
- Ask for unlock pattern

If pattern is correct:
    - Ask for fingerprint
    - If fingerprint matches:
        "Phone unlocked"
    - Else:
        "Fingerprint mismatch"
Else:
    "Wrong pattern"
"""

db_pattern = "v"

db_fingerprint = "zzzzvvvv"

user_pattern = input("enter pattern: ")

if db_pattern == user_pattern:
    user_fingerprint = input("enter fingerprint: ")
    if db_fingerprint == user_fingerprint:
        print("Phone unlocked")
    else:
        print("Fingerprint mismatch")
else:
    print("Wrong pattern")