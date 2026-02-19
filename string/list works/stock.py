"""
add 5 to 2 lists stock_list1 and stock_list2 and all new values in updated_stock_list
"""

stock_list1 = [10,11,12,13,14,15]

stock_list2 = [20,21,22,23,24,25]

stock_list1.extend(stock_list2)

updated_stock_list = []

for num in stock_list1:

    updated_stock_list.append(num+5)

print(updated_stock_list)

