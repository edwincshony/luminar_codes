# 12. GCD (Greatest Common Divisor) of two numbers

gcd = 1

number1 = 50
number2 = 80

if number1 > number2:

    smallest = number2

else:

    smallest = number1

for i in range(1,smallest+1):

    if number1 % i == 0 and number2 % i == 0:

        gcd = i


print(gcd)

# Use Euclidean algorithm:

# a = 50
# b = 80

# while b != 0:
#     a, b = b, a % b

# print(a)