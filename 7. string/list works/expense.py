#jan - dec 2025

expense_by_month = [1000,2000,1500,1500,1400,1477,1566,1489,1589,1478,1269,1478]

sum = 0

for exp in expense_by_month:

    print(exp)

    sum += exp

avg = sum / len(expense_by_month)

print(f"sum is {sum}")
print(f"avg is {avg}")
