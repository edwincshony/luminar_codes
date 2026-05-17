# Two pair sum- index wise

arr = [2,3,5,7]

org_arr = arr

arr.sort()

target = 8

left = 0

is_found = False

right = len(arr)-1

while(left<right):

    current_sum = arr[left] + arr[right]

    if current_sum == target:

        print(org_arr.index(arr[left]),org_arr.index(arr[right]))
        is_found = True
        break

    elif current_sum < target:

        left += 1

    else:

        right -= 1

