# 6. W.A.P (Write A Program) to display product of even numbers from 10 to 25

pro = 1

for i in range(10,26):

    if i % 2 == 0:

        pro *= i

print(pro)