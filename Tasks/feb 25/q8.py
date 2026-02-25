"""
8. From a given list of numbers, create a new list containing only numbers greater than 50 using list comprehension.

"""

lst = [1,2,56,78,90]

new_lst = [i for i in lst if i > 50]

print(new_lst)