"""
6.  Write a program to count how many even numbers are present in a
    list.
"""


my_list = [1,2,3,4,5,6,12,8,9,10]

even_count = 0

for number in my_list:

    if number % 2 == 0:

        even_count += 1


print(even_count)
