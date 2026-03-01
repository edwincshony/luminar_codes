"""5. Use a lambda function with filter() to get all even numbers from a list.
"""

lst = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda num: num % 2 == 0,lst))

print(even_numbers)