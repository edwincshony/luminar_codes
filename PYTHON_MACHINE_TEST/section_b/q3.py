"""13. Write a function to check whether two strings are anagrams.
"""

w1 = "eat"
w2 = "tea"

ana = False

for w in w1:

    if w in w2:

        ana = True
print(ana)

# good logic

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
