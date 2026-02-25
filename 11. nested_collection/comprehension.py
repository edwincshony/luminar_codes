# easy way for creating a sequence from another sequence

#list => list comprehension
#tuple => tuple comprehension
#set => set comprehension
#dict => dict comprehension

#syntax

# [left middle right]

# [return iteration condition]

arr = [10,12,13,14,15]

squares = [num**2 for num in arr]

print(squares)

cubes = [num**3 for num in arr]

print(cubes)

add_ten = [num+10 for num in arr]

print(add_ten)

