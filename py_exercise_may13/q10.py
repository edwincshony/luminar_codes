# 10. Common divisors of two numbers

number1 = 50
number2 = 80

min_num = min(number1,number2)

for i in range(1,min_num+1):

    if number1 % i == 0 and number2 % i == 0:

        print(i,end=" ")

