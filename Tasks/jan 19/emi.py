print("----------Program for Calculating EMI Calculation----------")


principal_amount = 100000

annual_rate = 13 

n = 3 # n: Loan Tenure (number of months for repayment). 

# Convert annual interest rate to monthly rate
monthly_interest_rate = annual_rate / (12 * 100)

emi = (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** n) / ((1 + monthly_interest_rate) ** n - 1)

print(emi)