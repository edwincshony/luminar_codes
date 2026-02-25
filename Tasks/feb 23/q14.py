"""
14. Create a dictionary from two lists (one list of keys and one list of values).


"""

lst1 = ["edwin","sreerag","gopi","rahul"]

lst2 = [50,15,45,89]

final_dict = {}

for i in range(len(lst1)):

    final_dict[lst1[i]] = lst2[i]

print(final_dict)

#using zip approach


# result = dict(zip(lst1,lst2))

# print(result)

