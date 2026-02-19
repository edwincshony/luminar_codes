"""
create a dictionary of product with attribute
id, title, price, avl_qty
"""

product = {"id":12,"title":"frooti","price":20,"avl_qty":15,"id":13}

print(product["title"])

product["avl_qty"] = product["avl_qty"] + 10

product["code"] = "sku12"

print(product)

if "offer" in product:

    print("yes")

else:

    print("no")