"""7. Write a program to remove duplicates from a list.
"""

lst = [10,11,12,11,14,15,14,15,18,15]

lst.sort()
new=[]
prev = 0

next = prev + 1

while(prev<len(lst)-1):

    diff = lst[next] - lst[prev]

    if diff != 0:

        new.append(lst[prev])

    prev += 1
    next = prev + 1
    
# add last element
if lst:
    new.append(lst[-1])

print(new)


# set very easy
lst = [10,11,12,11,14,15,14,15,18,15]
new = list(set(lst))
print(new)

# Cleaner version:
lst = [10,11,12,11,14,15,14,15,18,15]

new = []
seen = set()

for num in lst:
    if num not in seen:
        new.append(num)
        seen.add(num)

print(new)
