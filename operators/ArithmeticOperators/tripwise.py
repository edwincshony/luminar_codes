head_count = 5

bill_amount = 237

# 8% gst on bill amount

gst = 8

gst_adjusted_bill = bill_amount + (gst/100)*bill_amount

individual_split = gst_adjusted_bill / head_count

print("Individual split amount is:",individual_split)