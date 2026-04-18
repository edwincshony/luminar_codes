"""
def linear_search(arr,target):

    is_present = False

    for num in arr:

        if num == target:

            is_present = True

            break

    return is_present

print(linear_search([1,2,5,6],15))
"""

class LinearSearch:

    def solution(self,arr,element):

        is_present = False

        for num in arr:

            if num == element:

                is_present = True

                break

        return is_present

ls_instance = LinearSearch()

arr = [10,20,15,14,89,12]

element = 5699

print(ls_instance.solution(arr,element))
