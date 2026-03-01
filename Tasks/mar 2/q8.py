"""8. Write a Python program to count the number of words in a file.
"""

fr = open("Tasks\\mar 2\\q8file.txt")

count = 0

for line in fr:

    print(line)

    words = line.split()

    count += len(words)

print("Number of words is:",count)