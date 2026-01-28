"""
8. Restaurant Order System
------------------------------------
Task:
- Ask for table number

If table exists:
    - Ask for food availability
    - If food available:
        "Order placed"
    - Else:
        "Item out of stock"
Else:
    "Invalid table number"
"""

db_tables_nos = [10,11,12]

table_number = int(input("enter table number: "))
if table_number in db_tables_nos:
    food_availability = input("enter food availability (Y/N): ")
    if food_availability == "Y":
        print("Order placed")
    elif food_availability == "N":
        print("Item out of stock")
    else:
        print("invalid...")
else:
    print("Invalid table number")