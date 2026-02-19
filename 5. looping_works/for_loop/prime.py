"""
Logic:
A prime number is greater than 1 and has no divisors other than 1 and itself.
To check this, we test whether the given number is divisible by any integer between 2 and number − 1.

If any such divisor exists, the number is not prime.

If no divisor is found, the number is prime.

we are purposefully ignoring 1 and the number we got from user
"""

number = int(input('enter number: '))

is_prime = False

for i in range(2,number):

    if number % i == 0:

        is_prime = True

        break

if is_prime == False:

    print("Prime")

else:

    print("Not Prime")

