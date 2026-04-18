#23. Write a program using lambda, map, and filter to process a list of numbers.


# map(function,iterable) = Apply a function to every item in a list.

arr = [1,2,3,4,5,6]

square = lambda num:num**2

result = list(map(square,arr))

print(result)

# filter(function,iterable) = Select only items that meet a condition.

arr = [1,2,3,4,5,6]

gt_2 = lambda num:num>2

result = list(filter(gt_2,arr))

print(result)

# reduce (function,iterable) = applies a function increasingly to the elements of an iterable and returns a single final value.

# functools.py > reduce

from functools import reduce
arr = [10,11,12,13,14,15,16]

result = reduce(lambda n1,n2:n1*n2,arr)

print(result)