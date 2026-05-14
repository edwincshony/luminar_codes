# 19. Armstrong number

number = 0
count=0
tot=0
org_num_count = number
org_num_work = number

while(org_num_count!=0):

    org_num_count //= 10

    count += 1

while(org_num_work!=0):

    digit = org_num_work % 10

    tot = tot + digit ** count

    org_num_work //= 10

if tot == number:

    print("Armstrong number")

else:

    print("Not Armstrong number")




  