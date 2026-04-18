numbers = [1,2,89,9000,700,4]

slargest = float('-inf')
largest = float('-inf')

for num in numbers:

    if num > largest:

        slargest = largest

        largest = num

    elif num > slargest and num != largest:

        slargest = num

print(largest)
print(slargest)