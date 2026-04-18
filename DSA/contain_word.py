source = "edwin"
target = "win"

p1 = 0 # pointer to track source
p2 = 0 # pointer to track target

while(p1<len(source) and p2<len(target)):

    if source[p1] == target[p2]:

        p2 += 1

    p1 +=1

print(p2 == len(target))