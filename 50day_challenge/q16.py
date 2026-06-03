def sum_list(lst):

    result = 0

    for item in lst:

        if type(item) is list:

            result += sum_list(item)

        else:

            result += item

    return result

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

# def sum_list(nested_list):
#      return sum(sum(lst) for lst in nested_list) 
# print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))