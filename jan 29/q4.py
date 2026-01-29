"""
4. Write a program to calculate the sum of numbers from 1 to a number using a while loop.

"""

num = int(input("enter number: "))

i = 1

sum = 0

while(i<=num):

    sum = sum + i
    
    i = i + 1

print(sum)