"""
greatest common divisor from 2 numbers
8 and 12

common divisors = 1 2 4 

gcd = max(1,2,4) = 4
"""


number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

if number1<number2:

    smallest = number1

else:

    smallest = number2

gcd = 1

for i in range(1,smallest+1):

    if number1 % i == 0 and number2 % i == 0:

        gcd = i

print(f"GCD of numbers {number1} and {number2} is {gcd}")