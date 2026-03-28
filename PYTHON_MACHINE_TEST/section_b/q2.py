"""12. Write a program to sort a list without using built-in sort().
"""
numbers = [1,2,89,100,500,4]

n = len(numbers)

for i in range(n):

    for j in range(0,n-i-1):

        if numbers[j] > numbers[j+1]:

            numbers[j],numbers[j+1] = numbers[j+1],numbers[j] 

print(numbers)