"""
3. Online Shopping – Coupon Check
------------------------------------
Task:
- Ask for coupon code

If coupon code is valid:
    - Ask for cart amount
    - If amount ≥ 1000:
        "Coupon applied"
    - Else:
        "Minimum purchase not met"
Else:
    "Invalid coupon"
"""
db_coupon_code = "code"

coupon_code = input("enter coupon code: ")

if db_coupon_code == coupon_code:
    cart_amount = int(input("enter cart amount: "))
    if cart_amount >= 1000:
        print("Coupon applied") 
    else:
        print("Minimum purchase not met")
else:
    print("Invalid coupon")