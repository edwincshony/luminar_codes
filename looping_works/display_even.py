number = int(input("enter number: "))

while(number!=0):

    last_digit = number % 10

    if last_digit % 2 == 0:

        print(last_digit)

    number = number // 10