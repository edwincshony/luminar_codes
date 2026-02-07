year = int(input("enter year:"))
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("non leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("non leap year")