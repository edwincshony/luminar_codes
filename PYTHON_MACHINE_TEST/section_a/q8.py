"""8. Write a program to find the sum of digits of a number.
"""

number = 555

total_sum = 0

while number!=0:

    ld = number % 10
    total_sum = total_sum + ld
    number //= 10

print(total_sum)