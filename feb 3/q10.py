"""
10. Count the number of digits in a given number using a for loop.
"""

number = int(input("enter number: "))

count = 0

for i in str(number):

    count += 1

print(count)