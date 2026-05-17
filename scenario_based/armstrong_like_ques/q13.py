# 3. Spy Number

# A number is a Spy number if the sum of its digits equals the product of its digits.

# Input: n = 1124  
# Output: Spy  

# Explanation: Sum = 1+1+2+4 = 8  
# Product = 1×1×2×4 = 8

n = 1124

total_s = 0
total_p = 1

org_s = n
org_p = n

while(org_s!=0):

    ld = org_s % 10
    total_s = total_s + ld
    org_s //= 10

while(org_p!=0):

    ld = org_p % 10
    total_p = total_p * ld
    org_p //= 10

if total_s == total_p:

    print("Spy")

else:

    print("not Spy")