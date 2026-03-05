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




#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

limit = int(input("enter the limit: "))

prev = 0

current = 1

print(prev,end=" ")

print(current,end=" ")

for i in range(0,limit-2): # already two numbers printed 0 and 1, so only 8 remain so limit - 2

    next  = prev + current
    
    print(next,end=" ")

    prev = current

    current = next


"""
find whether number exist in fibonacci series
"""

"""
prev    → previous Fibonacci number
current → current Fibonacci number (the one we check)
next    → next Fibonacci number

"""
# my method easy

def is_fibonacci_number(number):
    is_fibo = False

    if number < 0:
        return is_fibo

    prev = 0
    current = 1

    while current <= number:
        if current == number:
            is_fibo = True
            break

        next = prev + current
        prev = current
        current = next

    return is_fibo



# print(is_fibonacci_number())
"""
find whether number exist in fibonacci series
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393
"""
# sir method

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

