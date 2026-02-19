"""
sales report
"""
#display day wise sales
# total_sale
# display avg_sales
# display day where sales < avg_sales

sales={"sun":21000,"mon":21800,"tue":21800,"wed":21980,"thur":21600,"fri":21820,"sat":21900}

# sales={"sun":100,"mon":100,"tue":100,"wed":100,"thur":100,"fri":100,"sat":100}
total_sale=0
found = False
for key in sales:
    print(key,sales[key])
    total_sale+=sales[key]
print("total_sale:",total_sale)
avg=total_sale/len(sales)
print("avg sale:",avg)  
for key in sales:
    if sales[key]<avg:
        print(key)
        found = True
       
if found == False:

    print("poda all above average")