"""16. Write a program to find common elements between two lists.
"""

lst1 = [10,11,12,13,14]

lst2 = [8,11,14,15,16]

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