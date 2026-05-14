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
# “Keep looping as long as there are letters left in the source word and we still have letters left to find in the target word.”

    if source[p1] == target[p2]:

        p2 += 1

    p1 += 1

print("Kangaroo word status:",p2 == len(target)) #👉 Means: all characters of target were found

# p2 == len(target) (3 == 3), which means all letters in "win" were found in order inside "edwin".
# So print("Kangaroo word status:", p2 == len(target)) prints: Kangaroo word status: True



