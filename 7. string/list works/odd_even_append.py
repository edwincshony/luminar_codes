"""
w.a.p to create 2 list even_list, odd_list
"""

numbers = [10,1,5,89,15,5,9]

even_list = []

odd_list = []


for num in numbers:

    if num % 2 == 0:

        even_list.append(num)

    else:

        odd_list.append(num)

print(f"Even numbers are {even_list}")
print(f"Odd numbers are {odd_list}")
