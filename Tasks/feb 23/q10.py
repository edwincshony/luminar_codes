"""
10. Given a set of numbers, remove all elements greater than 50.

"""

st = {10,20,11,55,45,58,89,120,47,51,124}

new_set = set()

for num in st:

    if num < 50:

        new_set.add(num)

print(new_set)

        

