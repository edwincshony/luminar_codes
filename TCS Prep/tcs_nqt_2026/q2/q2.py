# try:
    # doubt full code
hours = int(input())
if hours <= 0:
    print("error")
elif hours <= 2:
    charge = hours * 100
    print(charge)
elif hours <= 5:
    charge = 200 + (hours - 2) * 50
    print(charge)
else:
    charge = 200 + 150 + (hours - 5) * 20
    print(charge)
# except ValueError:
#     print("error")