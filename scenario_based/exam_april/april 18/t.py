
s = "VCDM"

Letters={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

n=len(s)

sum=0

i=0

while(i<n):

    if i<n-1 and Letters[s[i]]<Letters[s[i+1]]:

        sum+=Letters[s[i+1]]-Letters[s[i]]

        i+=2

    else:

        sum+=Letters[s[i]]

        i+=1

print(sum)