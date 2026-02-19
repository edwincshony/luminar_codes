"""
2 words in loop

break = exit from loop
continue = skip current iteration
"""

for i in range(1,10):

    if i == 5:

        break

    print(i)

print("THE END\n")

for i in range(1,10):

    if i == 5:

        continue

    print(i)

print("THE END")