# good logic

"""
is_ana = sorted(word1) == sorted(word2)
print(is_ana)
"""

word1 = "silent"
word2 = "listen"

if len(word1) != len(word2):
    is_anagram = False
else:
    is_anagram = True
    for ch in word1:
        if word1.count(ch) != word2.count(ch):
            is_anagram = False
            break

print(is_anagram)



















word1 = "silent"

word2 = "listen"

is_anagram = True

for ch in word1:

    if word2.find(ch) == -1:

        is_anagram = False

        break

print(is_anagram)




