# inverted + full pyramid code combined


for row in range(5, 0, -1):

    for sp in range(0, 5 - row):

        print(" ", end="")

    for col in range(0, row):

        print("* ", end="")

    print()

for row in range(5,0,-1):

    for sp in range(1,row):

        print(" ",end="")

    for col in range(1,5-row+2):

        print("* ",end="")

    print()