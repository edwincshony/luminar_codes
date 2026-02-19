"""
4.  Write a program to find the largest element in a list.
"""

my_list = [10,20,30,170,50]

largest = my_list[0]

for number in my_list:

    if number > largest:

        largest = number

print(largest)
