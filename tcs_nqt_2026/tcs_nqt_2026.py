purchase_value = float(input("enter the purchase value: "))

if purchase_value < 0:

    print("Error")
    exit()

elif purchase_value >= 5000:

    discount_rate = purchase_value -  (15/100 * purchase_value)

elif purchase_value < 5000 and purchase_value >= 1000:

    discount_rate = purchase_value - (10/100 * purchase_value)

elif purchase_value < 1000:

    discount_rate = purchase_value - (5/100 * purchase_value)

print(f"{discount_rate:.3f}")


#safe

purchase_value = float(input("enter the purchase value: "))

if purchase_value < 0:
    print("Error")
else:
    if purchase_value >= 5000:
        discount_rate = purchase_value * 0.85
    elif purchase_value >= 1000:
        discount_rate = purchase_value * 0.90
    else:
        discount_rate = purchase_value * 0.95

    print(f"Final payable amount is: {discount_rate:.2f}")