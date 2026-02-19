"""
9.  Write a program to search for an element in a list (take input from
    user).
"""


my_list = list(map(int, input("Enter numbers separated by space: ").split()))

"""
1️⃣ input("Enter numbers separated by space: ")

Purpose: Take input from the user.

Example input:

10 20 30 40


⚠️ Important: input() always returns a string

So result is:

"10 20 30 40"

2️⃣ .split()

Purpose: Split string into words using spaces.

"10 20 30 40".split()


Result:

['10', '20', '30', '40']


Now you have a list of strings, not numbers.

3️⃣ map(int, ...)

Purpose: Convert each item to integer.

map(function, iterable)

Here:

map(int, ['10','20','30','40'])


It applies:

int('10'), int('20'), int('30'), int('40')


Result (conceptually):

10, 20, 30, 40


⚠️ But map() returns a map object (not a list yet).

4️⃣ list(...)

Purpose: Convert the map object into a real list.

list(map(...))


Final result:

[10, 20, 30, 40]

summary

input → string
split → list of strings
map → convert each to int
list → final integer list

"""

target = int(input("Enter number to search: "))

if target in my_list:
    print("Element found")
else:
    print("Element not found")


    
