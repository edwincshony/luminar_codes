"""
*args = receives any number of parameter as tuple
"""

def add(*args): #args=(10,20,30)

    #args => will be of type tuple

    return sum(args)

print(add(10,20))
# print(add(10,20,30,40))

def largest_number(*args):

    return max(args)

# print(largest_number(10,20,30,50))
# print(largest_number(10,20,30,150))

def count_of_evens(*args):

    # count = 0

    # for num in args:

    #     if num % 2 == 0:

    #         count += 1

    # return count

    evens = [num for num in args if num%2==0]

    return len(evens)

print(count_of_evens(1,2,3,4,5))

def count_of_odd(*args):

    odds = [num for num in args if num%2!=0]

    return len(odds)

print(count_of_odd(10,11,12,13,14,15,16))

def product_of_nums(*args:tuple):

    product = 1

    for num in args:

        product = product * num

    return product

print(product_of_nums(1,2,3,4,5,6,7))