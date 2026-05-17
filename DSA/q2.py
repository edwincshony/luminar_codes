# lst = [10,11,12,11,13,15,14,13]

# 10 11 11 12 13 13 14 15

# # find duplicate numbers without using any predifned methods

# lst.sort()

# for prev in range(0,len(lst)-1):

#     next = prev + 1

#     diff = lst[next] - lst[prev]

#     if diff == 0:

#         print(lst[prev])


def duplicate(arr):

    arr.sort()

    # duplicate = []

    for prev in range(0,len(arr)-1):

        next = prev + 1

        difference = arr[next] - arr[prev]

        if difference == 0:

            print(arr[prev])

            # duplicate.append(arr[prev])

    # print(duplicate)

duplicate([10,11,12,11,13,15,14,13])

    


