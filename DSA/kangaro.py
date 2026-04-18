"""Alone 
 Lone
Blossom 
 Bloom
Capable 
 Able
"""
# The program scans "encourage" and checks if it can find "urge" letter by letter in the same order.
source = "edwin"
target = "win"

p1 = 0 # pointer to track source
p2 = 0 # pointer to track target

while(p1<len(source) and p2<len(target)):

    if source[p1] == target[p2]:

        p2 += 1

    p1 += 1

print("Kangaroo word status:",p2 == len(target)) #👉 Means: all characters of target were found



