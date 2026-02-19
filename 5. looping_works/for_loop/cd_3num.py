number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
number3 = int(input("enter number3: "))


if number1<number2 and number1<number3:

    smallest = number1

elif number2<number1 and number2<number3:

    smallest = number2

else:

    smallest = number3

for i in range(1,smallest+1):

    if number1 % i == 0 and number2 % i == 0 and number3 % i == 0:

        print(i)

