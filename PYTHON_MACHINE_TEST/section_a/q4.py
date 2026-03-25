"""4. Write a program to count vowels and consonants in a string.
"""

word = "aeiou"

v_count = 0

c_count = 0

VOWELS = "aeiouAEIOU"

for ch in word:

    if ch not in VOWELS:

        c_count += 1
    else:

        v_count += 1

print(v_count)
print(c_count)