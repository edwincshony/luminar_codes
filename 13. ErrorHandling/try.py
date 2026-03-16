age = int(input('enter age: '))

if age<18:

    raise Exception("invalid age")

else:

    print("granted")