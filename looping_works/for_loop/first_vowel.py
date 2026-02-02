"""
w.a.p to display first vowel character in a word
"""

word = "pythonprogramming"

VOWELS = "aeiouAEIOU"

for ch in word:

    if ch in VOWELS:

        print(ch)

        break