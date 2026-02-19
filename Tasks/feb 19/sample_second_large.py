numbers = [17,14, 46, 47, 86,17,17, 92, 52, 48, 36, 66, 85]

largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')

for num in numbers:

    if num > largest:

        third_largest = second_largest

        second_largest = largest
        
        largest = num
    
    elif num > second_largest and num != largest:

        third_largest = second_largest

        second_largest = num

    elif num > third_largest and num != largest and num != second_largest:

        third_largest = num
print(largest)
print(second_largest)
print(third_largest)