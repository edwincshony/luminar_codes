"""5. Write a program to print Fibonacci series up to N terms.
"""

# 0 1 1 2 3 5 8 13 21 34 

prev = 0

current = 1

limit = int(input("enter limit: "))

print(prev,end=" ")
print(current,end=" ")

for i in range(0,limit-2):

    next = prev + current

    print(next,end=" ")

    prev = current

    current = next