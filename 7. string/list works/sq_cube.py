"""
w.a.p create two list squares_list and cube_list
"""


numbers = [1,2,3,4,5]

squares_list = []

cube_list = []

for num in numbers:

    squares_list.append(num**2)

    cube_list.append(num**3)

print(squares_list)

print(cube_list)