"""
4. Write a program to calculate the sum of even numbers between 1 and 100 using a while loop.

"""

i = 1

even_sum = 0

while(i<=100):

    if i % 2 == 0:

        even_sum = even_sum + i

    i += 1

print(even_sum)

# 1 2 3 4 5 6 7 8 9 10

