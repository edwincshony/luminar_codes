# pip = tool used to manage python packages

# pip list = list all packages

# pip --version

# mysql-connector-python


# arr = [3,2,4]

# target = 6

# arr.sort()

# found = False

# left = 0

# right = len(arr) - 1

# while(left<right):

#     current_sum = arr[left] + arr[right]

#     if current_sum == target:

#         print(left,right)

#         found = True

#         break

#     elif current_sum < target:

#         left += 1

#     else:

#         right -= 1

# if found == False:

#     print("no pair")

# arr = [3,2,4]
# target = 6

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i, j)

arr = [2,3,4]
target = 6

seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        print(seen[complement], i)
    seen[num] = i