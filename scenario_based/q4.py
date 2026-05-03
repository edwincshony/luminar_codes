"""
4. First Non-Repeating Character
s = "aabbccdeff"
Task: Find the first non-repeating character.
"""
    
s = "aabbccdeff"

freq = {}

for l in s:

    if l in freq:

        freq[l] += 1

    else:

        freq[l] = 1
result = None
for l in s:

    if freq[l] == 1:

        result = l
        break

print(result)