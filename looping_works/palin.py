number = 11

result = 0

number_copy = number

while(number!=0):

    digit = number % 10

    result = result * 10 + digit

    number //= 10

if result == number_copy:

    print("pal")

else:

    print("not")

