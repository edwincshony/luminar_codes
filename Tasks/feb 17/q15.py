"""
15. Write a program to check whether a list is a palindrome.
"""
my_list = [10,20,30,20,10]

if my_list == my_list[::-1]:

    print("Palindrome")
    
else:
    print("Not Palindrome")
