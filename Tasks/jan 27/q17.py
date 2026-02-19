"""
17. Write a program to calculate discount eligibility based on purchase amount.
* Above 5000 → 20% discount
* 2000–5000 → 10% discount
* Below 2000 → No discount
"""

purchase_amount = int(input("enter purchase amount: "))

if purchase_amount > 5000:
    print("20% discount")
elif purchase_amount >= 2000 and purchase_amount <= 5000:
    print("10% discount")
elif purchase_amount < 2000:
    print("No discount")

