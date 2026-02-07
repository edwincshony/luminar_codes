"""
read 3 mark m1,m2,m3 each out of 50
find total
display A if total > 140
display B if total in range of 130 - 140
display C if total in range of 120 - 130
display fail anything below 120
grace mark 2 % of total marks

"""

mark1 = int(input("Enter mark1: "))

mark2 = int(input("Enter mark2: "))

mark3 = int(input("Enter mark3: "))

total_marks = mark1 + mark2 + mark3

# grace_marks = ((2/100) * total_marks)

# final_mark_after_grace = total_marks + grace_marks

# if final_mark_after_grace > 140:
#     print("A Grade")
# elif final_mark_after_grace >= 130 and final_mark_after_grace <= 140:
#     print("B Grade")
# elif final_mark_after_grace >= 120 and final_mark_after_grace < 130:
#     print("C Grade")
# elif final_mark_after_grace < 120:
#     print("Fail")

if total_marks > 140:
    print("A Grade")
elif total_marks > 130:
    print("B Grade")
elif total_marks > 120:
    print("C Grade")
else:
    print("Fail")
