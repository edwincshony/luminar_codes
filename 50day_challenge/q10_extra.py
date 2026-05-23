def convert_numbers(lst):

    result = []

    for num in lst:

        formatted = f"{num:,}"

        result.append(formatted)

    return result

print(convert_numbers(lst = [1000000, 2356989, 2354672, 9878098]))

    

