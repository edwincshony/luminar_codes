# 0, 1, 1, 2, 3, 5, 8, 13, 21

limit = int(input("enter limit: "))

prev = 0

current = 1

print(prev,end=" ")
print(current,end=" ")

for i in range(0,limit-2):

    next = prev + current

    print(next,end=" ")

    prev = current

    current = next

def is_fibonnaci(number):

    is_fibo = False

    if number < 0:

        return is_fibo

    prev = 0

    current = 1

    while(current<=number):

        if current == number:

            is_fibo = True

            break

        next = prev + current

        prev = current

        current = next

    return is_fibo

print(is_fibonnaci(21))