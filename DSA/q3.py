lst1 = [10,11,12,13,14]

lst2 = [8,11,14,15,16]

# 21 feb 2026 offline class

# find common in each list


# i. for num in lst1:

#     if num in lst2:

#         print(num)

# ii. lst1_set = set(lst1)

# lst2_set = set(lst2)

# print(lst1_set.intersection(lst2_set))

# iii. extend approach merge lists and check for diff = 0 then common 

# lst1.extend(lst2)

# lst1.sort()

# print(lst1)

# for prev in range(0,len(lst1)-1):

#     next = prev + 1

#     diff = lst1[next] - lst1[prev]

#     if diff == 0:

#         print(lst1[prev])


lst1.sort()

lst2.sort()

p1 = 0
p2 = 0

while(p1<len(lst1) and p2<len(lst2)):

    if lst1[p1] == lst2[p2]:

        print(lst1[p1])
        p1+=1
        p2+=1

    elif lst1[p1] < lst2[p2]: #The smaller number cannot match later (lists are sorted).

        p1 += 1

    else: #Now lst2 has the smaller number.

        p2 += 1
"""
One-line rule

👉 Move the pointer that has the smaller number
👉 If equal → move both
"""