fr = open("12.file_operations\\orders\\orders.txt","r")

all_orders = [line.rstrip("\n") for line in fr]

orders_count = {o:all_orders.count(o) for o in all_orders}

print(orders_count)

orders_count_max = [[v,k] for k,v in orders_count.items()]

print(sorted(orders_count_max,reverse=True))

