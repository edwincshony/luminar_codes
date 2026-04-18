# 0 1 1 2 3 5 8 13 21 34

limit = int(input())

prev = 0

current = 1

print(prev,end=" ")
print(current,end=" ")

for  i in range(0,limit-2):

    next = prev + current

    print(next,end=" ")

    prev = current

    current = next
