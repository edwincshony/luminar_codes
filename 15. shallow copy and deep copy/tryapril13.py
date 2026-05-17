source = "edwin"
target = "win"

p1=0
p2=0

while p1<len(source) and p2<len(target):

    if source[p1] == target[p2]:

        p2+=1

    p1+=1

print("kangaroo status",p2==len(target))

