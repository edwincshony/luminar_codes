"""5. Use a lambda function with filter() to get all even numbers from a list.
"""
# 02-03-2026 offline class discusseed
lst = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda num: num % 2 == 0,lst))

print(even_numbers)

# def map() = from a collection of objects apply a functionality on all values
# def filter() = apply a specific condition and filter the values
# def reduce() = process all data and return a single output

# using map (but can be easily achieved using list comprehension)

# lst = [1,2,3,4,5]

# map_sqaures = list(map(lambda num: num ** 2,lst))

# print(map_sqaures)

