"""
sum of even number upto limit
"""

limit = int(input("enter number: "))

i = 1

sum = 0

while(i<=limit):

    if i % 2 == 0:

        sum = sum + i

    i = i + 1


print(f"Sum of even numbers upto {limit}:",sum)