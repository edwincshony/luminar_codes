# 5. Duck Number

# A number is a Duck number if it contains at least one zero, but not at the beginning.
# Input: n = 1023  
# Output: Duck  

# Explanation: Contains 0, but not at the start

n = 1023
nstr = str(n)

is_duck = False

if '0' in nstr and nstr[0] != '0':
    is_duck = True

print(is_duck)
