"""
6. Print the multiplication table of a given number using a for loop.

"""

number = int(input("enter number: "))

for i in range(1,11):

    print(f"{i} * {number} = {i*number}")