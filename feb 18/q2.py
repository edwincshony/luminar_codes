"""
2.  Count Method: Given the string “banana”, count how many times the
    letter “a” appears.
"""

word = "banana"

count = 0

for w in word:

    if w == 'a':

        count += 1

print(f"In word {word} letter 'a' appeared {count} times")