"""
Task 24 || Nested list || 26-02-2026

products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

1. display all product names
2. product with the highest price
3. display electronics products
4. display products where the brand is Apple
5. which category has most products
6. product with maximum stock
7. list all categories
"""

products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

all_prod_names = [p[1] for p in products]

print("all product names: ",all_prod_names)
print("------------")

prod_prices = max([p[4] for p in products])

max_price = [p[1] for p in products if p[4] == prod_prices]

print("product with the highest price: ",max_price)
print("------------")

ele_prod = [p[1] for p in products if p[3] == "Electronics"]

print("Electronics products: ",ele_prod)

print("------------")
apple_prod = [p[1] for p in products if p[2] == "Apple"]

print("Apple Products: ",apple_prod)

print("------------")

category_list  = [p[3] for p in products]


category_counts  = {c: category_list.count(c) for c in category_list}

print(category_counts )

language_count_list = [[v,k] for k,v in category_counts.items()]

print(sorted(language_count_list,reverse=True)) # maximum product category as a list

# max_prod_category = max(category_counts,key=category_counts.get) # chatgpt approach limitation returns only one value

# print("Maximum product category single: ",max_prod_category)

print("------------")

max_stock_value  = max([p[-1] for p in products])

products_with_max_stock  = [p[1] for p in products if p[-1] == max_stock_value ]

print(products_with_max_stock)

print("------------")

categories = [p[3] for p in products]

print(categories)