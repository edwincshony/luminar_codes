"""
6. Find how many times 2 appears in the list [1, 2, 2, 3, 4, 2, 5].


"""

c = 0

numbers = [1, 2, 2, 3, 4, 2, 5]

for num in numbers:

    if num == 2:

        c += 1

print(f"Number 2 appeared {c} times in the list")