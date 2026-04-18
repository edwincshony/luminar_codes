"""
ATM Withdrawal
Problem Statement 
Simulate an ATM PIN check:
•
User has 3 attempts to enter the correct PIN.
•
If correct, allow withdrawal.
•
If incorrect after 3 attempts, block the card.
Input Format Integer PIN entered by the user. If correct, an integer withdrawal amount.
Output Format Success message with amount or “Card blocked due to 3 incorrect attempts.”
Sample Input:
1111
1234
5000
Sample Output:
Incorrect PIN.
₹5000 withdrawn successfully.
"""

org_pin = 1234

for i in range(3):

    user_pin = int(input("Enter PIN: "))

    if user_pin == org_pin:

        print("₹5000 withdrawn successfully.")

        break
    else:

        print("Incorrect PIN.")
else:

    print("Card blocked due to 3 incorrect attempts.")
