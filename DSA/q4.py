"""two pair sum"""

"""arr = [2,3,4,5]

target = 8"""



arr = [2,3,4,5]

target = 8

arr.sort()

found = False

left = 0

right = len(arr) - 1

while(left<right):

    current_sum = arr[left] + arr[right]

    if current_sum == target:

        print(arr[left],arr[right])

        found = True

        break

    elif current_sum < target:

        left += 1

    else:

        right -= 1

if found == False:

    print("no pair")


"""two pair sum"""

"""arr = [2,3,4,5]

target = 8"""

# def two_pair(arr,target):

#     arr.sort()

#     is_found = False
#     left = 0

#     right = len(arr)-1

#     while(left<right):

#         current_sum = arr[left] + arr[right]

#         if current_sum == target:

#             print(arr[left],arr[right],"is the pair")

#             is_found = True
#             break

#         elif current_sum < target:

#             left+=1

#         else:

#             right-=1

#     if is_found == False:

#         print("No pair found")

# two_pair(arr=[2,3,4,5],target=10)



