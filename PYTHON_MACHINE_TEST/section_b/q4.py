"""14. Write a program to merge two lists and remove duplicates.
"""

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

new = []
seen = set()

for num in lst1 + lst2:

    if num not in seen:

        new.append(num)
        seen.add(num)

print(new)
