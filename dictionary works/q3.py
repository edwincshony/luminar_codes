"""
Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"

"""

acc_details = {"acc_no":455578956845,"holder_name":"EDWIN C SHONY","balance":15000}

acc_details["balance"] += 5000

if acc_details["balance"] > 2000:

    acc_details["balance"] -= 2000

else:

    print("insufficient balance")

print(f"Your balance is {acc_details["balance"]}")

if acc_details["balance"] < 1000:

    print("Low Balance")