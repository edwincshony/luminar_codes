class BinarySearch:

    def solution(self,arr,element):

        is_present = False

        low = 0

        upp = len(arr)-1

        while low <= upp:

            mid = (low + upp) // 2

            if element == arr[mid]:

                is_present = True

                break

            elif element < arr[mid]:

                upp = mid - 1

            elif element > arr[mid]:

                low = mid + 1

        return is_present
        
bs_instance = BinarySearch()

# arr = [10,11,12,13,14,15]

# element = 256

print(bs_instance.solution([10,11,12,13,14,15],15))

