"""
lambda function

definition: anoynomous function with a single expression

syntax:

var_name = lambda p1,p2:expression
"""

"""
traditonal function 

def add(n1,n2):

    return n1 + n2"""

# regular function with one expression converted to lambda, so def and function_name removed when converted to lambda

#lambda function

add = lambda n1,n2:n1+n2

print(f"Sum is: {add(100,200)}")

sub = lambda n1,n2:n1-n2

print(f"Difference is: {sub(100,200)}")

cube = lambda n: n ** 3

print(f"Cube is: {cube(2)}")

odd_even = lambda num: "Even" if num%2 == 0 else "Odd"

print(odd_even(3))

# create a lambda function is_positive return True if number is positive else return False

# is_positive = lambda num: True if num > 0 else False
is_positive = lambda num: num > 0
print(is_positive(89))

#def map() = from a collection of objects apply a functionality on all values
# def filter() = apply a specific condition and filter the values
# def reduce() = process all data and return a single output