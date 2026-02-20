manali = {

    "dijo": 300,
    "akshay": 1000,
    "edwin": 800,
    "alan": 15000,
    "manoj": 0,
    "supin": 0,
    "sreeyesh": 500

    }

total_expense = 0

for val in manali.values():

    total_expense += val

print(f"Total expense is: {total_expense}")

individual_split = total_expense/len(manali)

print(f"Individual split is {individual_split}")

spend_wise = {}

for key,value in manali.items():

    payment = individual_split - value

    spend_wise[key] = payment

print(spend_wise)