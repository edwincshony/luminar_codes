sales_report = {

    "sunday" : 18000,
    "monday" : 18000,
    "tue": 1500,
    "wed": 2900,
    "thurs": 15000,
    "fri": 19000,
    "sat": 2148
}
tot = 0
#display day wise sales
# total_sale
# display avg_sales
# display day where sales < avg_sales

# day with highest sale
# day with lowest sale

print(sales_report)

for val in sales_report.values():

    tot += val

print(tot/len(sales_report))

print("----------")

for key,val in sales_report.items():

    if val < (tot/len(sales_report)):

        print(key)

print("----------")

high = float('-inf')

for key,val in sales_report.items():


    if val > high:

        high = val
        high_key = key

print(high_key,high)

print("----------")

low = float('inf')

for key,val in sales_report.items():


    if val < low:

        low = val
        low_key = key

print(low_key,low)

print("----------")