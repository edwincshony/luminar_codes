"""
9. Write a program to find common elements in three different sets.

"""

st1 = {1,3,4,5}

st2 = {5,7,4,3}

st3 = {10,4,5,3}

result = st1.intersection(st2)

final_result = result.intersection(st3)

print(final_result)