"""
7.  Write a program to count how many odd numbers are present in a list.
"""

my_list = [1,2,3,4,5,6,12,8,9,10]

odd_count = 0

for number in my_list:

    if number % 2 != 0:

        odd_count += 1

print(odd_count)