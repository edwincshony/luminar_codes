"""
ABABC

print which repeats first
"""

word = "CCAABBC"
seen = set()
for w in word:
    if w in seen:
        print(w)
        break
    seen.add(w)
