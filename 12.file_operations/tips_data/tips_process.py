from csv import DictReader

fr = open("12.file_operations\\tips_data\\tips.csv")

# csv => list of dictionary [csv.py => DictReader]

data = list(DictReader(fr))

# daily tip with day: tip

day_wise_summary = {}

for t in data:

    day = t.get("day")
    tip = float(t.get("tip"))

    if day in day_wise_summary:

        day_wise_summary[day] += tip

    else:

        day_wise_summary[day] = tip

print(day_wise_summary)


# day with highest revenue

day_wise_bill = {}

for t in data:
    
    day = t.get("day")
    bill = float(t.get("total_bill"))

    if day in day_wise_bill:

        day_wise_bill[day] += bill

    else:

        day_wise_bill[day] = bill

day_wise_high  = [[v,k] for k,v in day_wise_bill.items()]

print(sorted(day_wise_high,reverse=True)[0][1])

# which customer giving more tip



