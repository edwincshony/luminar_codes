sales_report = {

    "sunday" : 18000,
    "monday" : 18000,
    "tue": 1500,
    "wed": 2900,
    "thurs": 15000,
    "fri": 19000,
    "sat": 2148
}

#display day wise sales
# total_sale
# display avg_sales
# display day where sales < avg_sales

# day with highest sale
# day with lowest sale

print(sales_report)

total_amount = 0

for key in sales_report:

    amount = sales_report[key]

    total_amount += amount

print(f"Total sale amount is {total_amount}")

avg_sales = total_amount/len(sales_report)

print(f"Average sale amount is {total_amount/len(sales_report)}")

for key in sales_report:

    if sales_report[key] < avg_sales:

        print(key)

print("--------------")

largest = float('-inf')

highest_day = None

for key in sales_report:

    if sales_report[key] > largest:

        largest = sales_report[key]

        highest_day = key

print(f"Day with highest sales: {highest_day} ({largest})")

print("-----------")

lowest = float('inf')

lowest_day = None

for key in sales_report:

    if sales_report[key] < lowest:

        lowest = sales_report[key]

        lowest_day = key

print(f"Day with lowest sales: {lowest_day} ({lowest})")






