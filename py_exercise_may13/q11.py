# 11. Common divisors of three numbers

number1 = 12
number2 = 18
number3 = 36

if number1 <= number2 and number1 <= number3:

    smallest = number1

elif number2 <= number1 and number2 <= number3:

    smallest = number2

elif number3 <= number1 and number3 <= number2:
     
     smallest = number3

for i in range(1,smallest+1):

    if number1 % i == 0 and number2 % i == 0 and number3%i==0:

            print(i,end=" ")
