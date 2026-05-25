def age_in_minutes():

    while True:

        yob = int(input("Enter the YOB: "))

        if len(str(yob))!=4:

            print("Enter a 4 digit number")

        elif yob < 1900:

            print("Input is invalid")

        elif yob > 2026:

            print("Input is invalid no future years")

        else:

            age_minutes  = (2026 - yob) * 525600

            return f"You are {age_minutes} minutes old"

print(age_in_minutes())