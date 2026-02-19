for row in range(6, 0, -1):

    for sp in range(0, 6 - row):

        print(" ", end="")

    for col in range(0, row):

        print("*", end="")

    print()
