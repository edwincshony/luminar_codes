"""
6. Reverse a given list without using reverse() method.

"""

lst = [10,20,30,40,50]

result = []

for i in range(len(lst)-1, -1, -1):

    result.append(lst[i])

print(result)

