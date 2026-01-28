"""
6. Bank Loan Eligibility
------------------------------------
Task:
- Ask for monthly income

If income ≥ 25,000:
    - Ask for credit score
    - If credit score ≥ 700:
        "Loan approved"
    - Else:
        "Low credit score"
Else:
    "Income not sufficient"
"""

monthly_income = int(input("enter monthly income: "))

if monthly_income >= 25000:
    credit_score = int(input("enter credit score"))
    if credit_score >= 700:
        print("Loan approved")
    else:
        print("Low credit score")
else:
    print("Income not sufficient")