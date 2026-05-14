# 1. Neon Number Check

# A number is a Neon number if the sum of digits of its square equals the number itself.

# Input: n = 9  
# Output: Neon  

# Explanation: 9^2 = 81 → 8 + 1 = 9

n = 1
total=0
result = n ** 2

while(result!=0):

    ld = result % 10
    total = total + ld
    #print(ld)
    result //= 10

if total == n:
    print("Neon")
else:
    print("Not Neon")

