# 2. Harshad (Niven) Number

# A number is a Harshad number if it is divisible by the sum of its digits.

# Input: n = 18  
# Output: Harshad  

# Explanation: 1 + 8 = 9 → 18 % 9 = 0

n = 18
total=0
org = n

while(n!=0):

    ld = n % 10
    total = total + ld
    #print(ld)
    n //= 10

if org % total == 0:
    print("Harshad")
else:
    print("Not Harshad")