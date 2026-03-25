"""9. Write a program to count frequency of each character in a string.
"""

"""word = "edwwin"

seen=[]

for ch in word:

    if ch not in seen:
        print(f"Frequency of {ch} is: {word.count(ch)}")
        seen.append(ch)"""

# efficient approach

word = "edwwin"
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in freq:
    print(f"Frequency of {ch} is: {freq[ch]}")