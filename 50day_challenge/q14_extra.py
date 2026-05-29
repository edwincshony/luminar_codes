def your_salary():

    monthly_salary = 0

    name = input("Enter teacher name: ")

    no_of_periods = int(input("Enter the number of periods taken: "))

    if no_of_periods < 100:

        monthly_salary = no_of_periods * 20

    else:

        overtime = no_of_periods - 100

        monthly_salary = (100*20) + (overtime * 25)

    return f"Teacher: {name},\nPeriods: {no_of_periods}\nGross salary: {monthly_salary}"

print(your_salary())