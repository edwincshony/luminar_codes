age = int(input('enter age: '))

if age<18:

    raise Exception("invalid age")
else:

    print("access granted")

# read a password
# if length of password is < 6 create a custom error is password invalid

password = input('enter password: ')

if len(password)<6:

    raise Exception("password invalid") # in java throw used instead of raise
else:

    print("access granted")