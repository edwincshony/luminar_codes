def your_vat():

    while True:

        try:

            amount = float(input("Enter the price of the item: "))

            vat_percent = float(input("Enter VAT percentage: "))

            vat = (vat_percent/100) * amount

            final_price = amount + vat
        
            return final_price
        
        except ValueError:

            print("Please enter valid numbers.")

print(your_vat()) 