"""
5. Write a Python program to print the multiplication table of a given number using a while loop.

"""

number = int(input("enter number: "))

i = 1

while(i<=10):

    print(f"{i} * {number} = {i*number}")

    # print(i,"*",number,"=",i*number) # without f string
 
    i = i + 1