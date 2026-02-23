"""

6. Given two sets, find the symmetric difference between them.

symmetric difference = (A U B) - (A ^ B)
symmetric difference = (A - B) u (B - A)

"""

st1 = {1,2,3}

st2 = {3,4,5,6}

common_set = st1.union(st2)
unique_set = st1.intersection(st2)

symmetric_set = common_set - unique_set

# result = st1.symmetric_difference(st2)

print(symmetric_set)

# print(result)

