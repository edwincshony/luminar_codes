"""
8.  Write a program to count positive and negative numbers in a list.
"""

my_list = [1,2,3,4,5,6,12,8,9,-9,-18]

pos_count = 0

neg_count = 0

for number in my_list:

    if number > 0:

        pos_count += 1

    else:

        neg_count += 1

print(pos_count)
print(neg_count)