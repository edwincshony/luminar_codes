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
tot=0
avg=0
for val in sales_report.values():
    tot += val
print(tot)
avg = tot/len(sales_report)
print(avg)

for key,val in sales_report.items():
    if val<avg:
        print(key)



highest = float('-inf')
highest_day = ""
for key,val in sales_report.items():
    if val>highest:
        highest = val
        highest_day = key
print(highest_day,highest)

highest = float('inf')
highest_day = ""
for key,val in sales_report.items():
    if val<highest:
        highest = val
        highest_day = key
print(highest_day,highest)