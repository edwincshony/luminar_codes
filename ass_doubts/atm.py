"""
✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"
"""

db_pin = 1234
db_balance = 1000

user_pin = int(input("enter user atm pin: "))

if db_pin == user_pin:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= db_balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")



