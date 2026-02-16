"""H,P,O"""
edwin_attendence = ["H","P","P","P","P","P","H","H","P"]

edwin_attendence[4] = "H"

for attendence in edwin_attendence:

    print(attendence)


holiday_count = 0
leave_count = 0
online_count = 0
present_count = 0

for at in edwin_attendence:

    if at == "H":

        holiday_count += 1

    elif at  == "L":

        leave_count += 1

    elif at == "O":

        online_count += 1

    elif at == "P":

        present_count += 1

print(holiday_count)
print(leave_count)
print(online_count)
print(present_count)


    

