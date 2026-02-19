"""
10. Write a program to print the list in reverse order (without using
    reverse method).
"""

my_list = [10,20,30,40,50,700]

# for i in range(5,-1,-1):

#     print(my_list[i],end=" ")

for i in range(len(my_list)-1,-1,-1):

    print(my_list[i],end=" ")
