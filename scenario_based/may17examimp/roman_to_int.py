s = "IV"

dict1 = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

i = 0

n = len(s)

res = 0

while(i<n):

    if i < n - 1 and dict1[s[i]] < dict1[s[i+1]]:

        res += dict1[s[i+1]] - dict1[s[i]]

        i += 2

    else:

        res += dict1[s[i]]

print(res)

# int to roman

num = 1994

values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

result = ""

i = 0

while num > 0:

    if num >= values[i]:

        result += symbols[i]

        num -= values[i]

    else:

        i += 1

print(result)