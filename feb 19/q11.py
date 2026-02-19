"""

Given a list of numbers [5, 12, 7, 20, 3, 18], create a new list that contains only the numbers greater than 10.
"""

numbers = [5, 12, 7, 20, 3, 18]

new_list = []

for num in numbers:

    if num > 10:

        new_list.append(num)

print(new_list)