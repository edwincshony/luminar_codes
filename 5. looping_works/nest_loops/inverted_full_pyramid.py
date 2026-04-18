for row in range(5, 0, -1):

    # print spaces
    for sp in range(5 - row):
        print(" ", end="")

    # print stars
    for col in range(row):
        print("*", end=" ")

    print()