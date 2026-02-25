"""two pair sum"""

"""arr = [2,3,4,5]

target = 10"""



arr = [2,3,4,5]

target = 10

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

