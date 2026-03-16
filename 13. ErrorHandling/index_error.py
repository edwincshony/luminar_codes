#list index out of range

lst = [1,2,3,4,5]
#      0 1 2 3 4

index = int(input("enter index to print value: "))

try:

    print(lst[index])

except Exception as e:

    # index = int(input("enter index to print value: "))

    # print(lst[index])

    print(e)

finally:

    print("Database commit")
