"""
w.a.p to create 2 list positive_list, negative_list
"""

numbers = [-1,-1,10,11,12,13,-13,-15,4,5]

positive_list = []

negative_list = []


for num in numbers:

    if num > 0:

        positive_list.append(num)

    elif num < 0:

        negative_list.append(num)

print(f"Postitive numbers are {positive_list}")
print(f"Negative numbers are {negative_list}")
