# abcd

# pqrs

# apbqcrds

#abcdef
#pqrs
#apbqcrdsef

#abcd
#pqrsef
#apbqcrdsef

# efficient version

w1 = "abcdef"
w2 = "pqrs"

result = ""

min_len = min(len(w1), len(w2))

for i in range(min_len):
    result += w1[i] + w2[i]

result += w1[min_len:] + w2[min_len:]

print(result)

# inefficient

w1 = "abcd"

w2 = "pqrsef"

result = ""


if len(w1) == len(w2):

    for i in range(0,len(w1)):

        result += w1[i] + w2[i]

    print(result)

elif len(w1) > len(w2):

    for i in range(0,len(w2)):

        result += w1[i] + w2[i]

    print(result + w1[len(w2):])

elif len(w1) < len(w2):

    for i in range(0,len(w1)):

        result += w1[i] + w2[i]

    print(result + w2[len(w1):])

