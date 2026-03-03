tips_data = [
    {"total_bill": 16.99, "tip": 1.01, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 8.77,  "tip": 2.00, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 26.88, "tip": 3.12, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 15.04, "tip": 1.96, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 14.78, "tip": 3.23, "sex": "Female", "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.27, "tip": 1.71, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 35.26, "tip": 5.00, "sex": "Female", "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 15.42, "tip": 1.57, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 18.43, "tip": 3.00, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 14.83, "tip": 3.02, "sex": "Female", "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 21.58, "tip": 3.92, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Dinner", "size": 2},
    {"total_bill": 10.33, "tip": 1.67, "sex": "Female", "smoker": "No",  "day": "Fri",  "time": "Lunch",  "size": 2},
    {"total_bill": 16.29, "tip": 3.71, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Lunch",  "size": 3},
    {"total_bill": 13.37, "tip": 2.00, "sex": "Female", "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 12.69, "tip": 2.31, "sex": "Male",   "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 17.92, "tip": 4.08, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 20.29, "tip": 2.75, "sex": "Female", "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 15.77, "tip": 2.23, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 39.42, "tip": 7.58, "sex": "Male",   "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 19.82, "tip": 3.18, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2}
]


#q1 highest total bill 

# approach 1

max_total_bill = max(t.get("total_bill") for t in tips_data)
print(max_total_bill)

# approach 2

max_tot_bill = max(tips_data,key=lambda x:x["total_bill"])

print(max_tot_bill.get("total_bill"))

#q2 most appeared day

# approach 1

day = [c.get("day") for c in tips_data]

day_count = {c:day.count(c) for c in day}

day_max = [[v,k] for k,v in day_count.items()]

print(sorted(day_max,reverse=True)[0])

# approach 2

days1 = [t.get("day") for t in tips_data]

most_common_day  = max(set(days1),key=lambda d:days1.count(d))

print(most_common_day)

#q3 count of marked as yes

#approach 1

count_as_yes = [c for c in tips_data if c.get("smoker") == "Yes"]

print(len(count_as_yes))

#approach 2

count_as_yes1 = list(filter(lambda x:x.get("smoker") == "Yes",tips_data))

print(len(count_as_yes1))

# tip given for the largest group size

max_size = max(c.get("size") for c in tips_data)
tip_given = [c.get("tip") for c in tips_data if c.get("size") == max_size]
print(tip_given) 

