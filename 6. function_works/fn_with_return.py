# function with parameter and return value

# if return used in function then only use print(function_name(arg1,arg2)) bcoz it has something to return


def addition(num1,num2):

    result = num1 + num2

    return result

print(addition(100,200))


def subtraction(num1,num2):

    result = num1 - num2

    print(result)

# print(subtraction(100,80)) #this is wrong 

subtraction(100,80)


"""
find whether number exist in fibonacci series
"""

def is_fibonacci_number(number):

    is_fibo = False

    prev = 0

    current = 1

    next = prev + current

    while(next<=number):

        next = prev + current

        prev = current

        current = next

        if next == number:

            is_fibo = True

            break

    return is_fibo


print(is_fibonacci_number(3))  #True
print(is_fibonacci_number(12))  #False

