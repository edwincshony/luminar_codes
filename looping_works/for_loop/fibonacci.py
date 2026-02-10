#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

limit = int(input("enter the limit: "))

prev = 0

current = 1

print(prev,end=" ")

print(current,end=" ")

for i in range(1,limit-1):

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

