"""
12. Write a program to count the frequency of each character in a string using a dictionary.


"""

s = "python"

freq = {}

for char in s:

    if char in freq:

        freq[char] = freq[char] + 1

    else:

        freq[char] = 1

print(freq)