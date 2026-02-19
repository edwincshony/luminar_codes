"""
A perfect number is defined as:

A number that equals the sum of its proper divisors.

Proper divisors = positive divisors excluding the number itself.

Example: 6

Divisors of 6:
1, 2, 3, 6

Proper divisors of 6 (excluding 6):
1, 2, 3

Sum of proper divisors:
1+2+3=6

Example: 28

Divisors of 28:
1, 2, 4, 7, 14, 28

Proper divisors of 28 (excluding 28):
1, 2, 4, 7, 14

Sum of proper divisors:
1+ 2+ 4+ 7+ 14 = 28
"""

number = int(input("enter number: "))

total_sum = 0

for i in range(1,number):

    if number % i == 0:

        # print(i)

        total_sum += i

# if total_sum == number:

#     print("perfect number")

# else:

#     print("Not perfect number")


print("Perfect number" if total_sum==number else "Not perfect number")




    