"""

5.  Write a program to find the smallest element in a list.
"""

my_list = [10,20,30,170,50]

smallest = my_list[0]

for number in my_list:

    if number < smallest:

        smallest = number

print(smallest)