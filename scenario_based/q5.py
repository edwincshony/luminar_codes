"""5. Group Anagrams
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Task: Group words that are anagrams together.
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_groups = {}

for word in words:
    # Sort the word to use as a key
    key = ''.join(sorted(word))
    
    if key in anagram_groups:
        anagram_groups[key].append(word)
    else:
        anagram_groups[key] = [word]

# Convert dictionary values to list
result = list(anagram_groups.values())

print(result)
