"""
Take numbers until user enters 0. Print sum.
"""

tot = 0

while True:

    num = int(input())

    tot += num

    if num == 0:

        break
print(tot)