orders = ["tea","coffee","idly","coffee","tea","dosa","tea","coffee"]

orders_count = {o:orders.count(o) for o in orders}

print(orders_count)

# normal approach

orders_count={}

for o in orders:

    orders_count[o] = orders.count(o)

print(orders_count)