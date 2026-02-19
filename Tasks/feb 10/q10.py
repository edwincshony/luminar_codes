"""
10. Write a function that takes a number as a parameter and returns True if it is a prime number, otherwise returns False.
"""

def is_prime(number):

    for i in range(2,number):

        if number % i == 0:

            return False
       

    return True
        
print(is_prime(9))