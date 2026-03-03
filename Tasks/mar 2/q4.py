"""4. Write a Python program to sort a list of tuples based on the second element using a lambda function.
"""
# 02-03-2026 offline class discusseed

lst = [(1, 3), (4, 1), (2, 2)]

# sorted_lst = sorted(lst, key=lambda tp: tp[1])
# print(sorted_lst)

lst.sort(key=lambda tup:tup[1])
print(lst)

