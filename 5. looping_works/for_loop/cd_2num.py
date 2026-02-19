"""
print common divisors of 2 numbers
"""

number1 = int(input('enter number1: '))
number2 = int(input('enter number2: '))


if number1>number2:

    smallest = number2

else:

    smallest = number1

for i in range(1,smallest+1):

    if number1 % i == 0 and number2 % i == 0:

        print(i)
