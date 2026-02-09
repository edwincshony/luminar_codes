"""
7. Write a function that takes a number as a parameter and returns the factorial of that number.

"""

def factorial(number):

    fact = 1

    for i in range(1,number+1):

        fact = fact * i

    return fact
    
print(factorial(5))