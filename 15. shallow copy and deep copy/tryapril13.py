arr = [1,2,3,4,5,6]

square = lambda num:num**2

res = list(map(square,arr))

print(res)

arr = [1,2,3,4,5,6]


filtter = lambda num:num>2

res = list(filter(filtter,arr))
print(res)

from functools import reduce

arr = [1,2,3,4,5,6]


resukt = reduce(lambda n1,n2:n1*n2,arr)

print(resukt)