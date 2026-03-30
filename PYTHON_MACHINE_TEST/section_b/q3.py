"""13. Write a function to check whether two strings are anagrams.
"""

def check_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(check_anagrams("listen", "silent"))  # True

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

# scene approach

def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


st1 = input("enter string1: ")
st2 = input("enter string2: ")

print("Anagrams" if check_anagrams(st1, st2) else "Not Anagrams")