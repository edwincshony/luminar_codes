#135

number = 135

length = len(str(135))

result = 0

while(number!=0):

    for i in range(length,0,-1):

        ld = number % 10
        
        result = result + (ld**i)

        number //= 10

print(result)
