# 2 = 24 2+22 = 24 
# 3 = 369   3+33+333 = 369 
# 4 = 4936   4+44+444+4444 = 4936

number = int(input("Enter number: "))  #3

term = " "

total = 0

for i in range(1,number+1): #1,3

    term = term + str(number) # " " + "3" = "3", "3"+"3"="33", "33"+"3"=333

    total = total + int(term)# 0+3=3, 3+33=36, 36+333=369

print(total)
