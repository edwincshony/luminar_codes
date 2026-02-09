"""
create a function smart_sub with 2 parameter n1,n2

return subtraction result as n1-n2 if n1>n2 else return n2-n1
"""

def smart_sub(n1,n2):

    if n1 > n2:

        return n1 - n2
    else:

        return n2 - n1
    
# print(smart_sub(20,8))

"""

create a function is_odd with param num return True if num is odd else return False
create a function is_even with param num return True if num is even else return False
create a function is_positive with param num return True if num is positive else return False
create a function is_zero with param num return True if num is zero else return False

"""

def is_odd(number):

    if number % 2 != 0:

        return True

    else:

        return False
    
print(is_odd(5))

def is_even(number):

    if number % 2 == 0:

        return True

    else:

        return False
    
print(is_even(2))

def is_positive(number):

    if number > 0:

        return True

    else:

        return False
    
print(is_positive(-2))

def is_zero(number):

    if number == 0:

        return True

    else:

        return False
    

    # return number == 0
    
print(is_zero(0))


def exponent(base,pow=2): # pow value set to 2 default

    result = base ** pow

    return result

print(exponent(2,pow=3)) #ultimate power to argument 

# this pgm print 2 ** 3 = 8


# create a function calculator with n1,n2,op

# if op == + return addition of n1, n2
# if op == - return sub of n1, n2
# if op == * return mul of n1, n2
# if op == / return divison of n1, n2

def calculator(num1,num2,op="+"):

    if op == "+":

        return num1 + num2
    
    elif op == "-":

        return num1 - num2
    
    elif op == "*":

        return num1 * num2
    
    elif op == "/":

        return num1 / num2
    
print(calculator(10,20,op="/"))
    

