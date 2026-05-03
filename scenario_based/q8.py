"""8. Find Duplicate in List (No Extra Space)
nums = [1, 3, 4, 2, 2]
Task: Find the duplicate number without using extra memory."""

# why not for i in range(len(nums)-1):
# Starting at 0 = “compare first item with last item” ❌
# Starting at 1 = “Compare current item with previous one”✅

nums = [1, 3, 4, 2, 2]
nums.sort()
dup=[]
for i in range(1,len(nums)):

    if nums[i] == nums[i-1]:
        dup.append(nums[i])

print(dup)


    
