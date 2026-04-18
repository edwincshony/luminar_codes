"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
 """
# first approach

# lst = [1,2,3,4,5]

# for i in range(1,len(lst)+1):

#     if i not in lst:

#         print(i)
        
#         break

# # if for loop hits break then for-else will not work

# # if for loop completes without break for-else will work

# else:

#     print(len(lst)+1,"is missing")


#second approach

# lst = [2,3,4,5]
# lst.sort()
# print(lst)
# for i in range(0,len(lst)-1):

#     difference = lst[i+1] - lst[i] 

#     if difference != 1: #if diff = 1 then no number missing, else: number is missing

#         print(f"{lst[i] + 1} is missing")

    
#3rd approach most relaible

# lst = [1,2, 3, 4, 5]
# s = set(lst)

# i = 1
# while True:
#     if i not in s:
#         print(i)
#         break
#     i += 1

def missing_least_number(arr):

    arr.sort()

    if arr[0] != 1:
        print(1, "is missing")
        return

    prev = 0

    next = prev + 1

    while(prev<len(arr)-1):

        diff = arr[next] - arr[prev]

        if diff != 1:

            print(arr[prev]+1,"is missing")

            return


        prev += 1

        next = prev + 1

    print(arr[-1]+1,"is missing")

missing_least_number([1,2,3,4]) 


# def missing_least_number(arr):

#     arr.sort()

#     for prev in range(0,len(arr)-1):
#         next = prev + 1
#         diff = arr[next] - arr[prev]

#         if diff != 1:

#             print(arr[prev]+1,"is missing")

#             break

#     else:

#         print(arr[-1]+1,"is missing")

# missing_least_number([2,3,4,5]) 

