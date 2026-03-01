"""4. Write a Python program to sort a list of tuples based on the second element using a lambda function.
"""
lst = [(1, 3), (4, 1), (2, 2)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)