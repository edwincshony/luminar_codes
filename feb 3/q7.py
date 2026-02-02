"""
7. Count the number of vowels in a given string using a for loop.

"""

word = input("enter string: ")

count = 0

VOWELS = "aeiouAEIOU"

for ch in word:

    if ch in VOWELS:

        count += 1

print(count)

        