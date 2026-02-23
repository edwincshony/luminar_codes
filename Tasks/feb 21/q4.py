"""

4. Write a program to check whether an element exists in a tuple or not.

"""

tup = (10,20,30,40,50)

search_element = int(input("Enter search element: "))


if search_element in tup:

    print("exists in tuple")

else:

    print("not exists in tuple")