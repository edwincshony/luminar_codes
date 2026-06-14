def unique_numbers(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    total_sum = sum(numbers)
    unique_sum = sum(unique)

    difference = total_sum - unique_sum

    if difference % 2 == 0:
        return numbers
    else:
        return unique

print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))