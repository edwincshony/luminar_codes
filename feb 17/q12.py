"""
12. Write a program to print elements present at even index positions.

zero is an even number

"""

my_list = [10,20,10,40,50,700]

        #   0  1  2  3  4   5

for i in range(0,len(my_list)):

    if i % 2 == 0:

        print(my_list[i])