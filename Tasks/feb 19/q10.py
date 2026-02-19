"""
Write a program to remove all duplicate elements from the list: [10, 20, 30, 20, 40, 10, 50] (Keep only unique values.)
"""

numbers = [10, 20, 30, 20, 40, 10, 50]

unique_list = list(set(numbers))

print(unique_list)