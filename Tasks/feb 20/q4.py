"""
4. Given a tuple (1, 2, 3, 4, 5), convert it into a list, add a new element, and convert it back to a tuple.

"""

tup = (1,2,3,4,5)

print(type(tup))

lst = list(tup)

print(type(lst))

lst.append(6)

final_tup = tuple(lst)

print(final_tup)